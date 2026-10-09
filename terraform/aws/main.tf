terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = "ap-southeast-2"
  profile = "juhoon"
}

# Find the latest Amazon Linux 2023 AMI (free tier eligible)
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023.*-x86_64"]
  }
}

resource "aws_security_group" "app_sg" {
  name        = "mining-monitor-sg"
  description = "Allow SSH from my IP and app port from anywhere"

  ingress {
    description = "SSH from my IP only"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["159.196.132.79/32"]
  }

  ingress {
    description = "App port"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "app_server" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t3.micro"
  key_name               = "juhoon-key"
  vpc_security_group_ids = [aws_security_group.app_sg.id]

  user_data = <<-USERDATA
    #!/bin/bash
    dnf install -y docker git
    systemctl start docker
    systemctl enable docker
    usermod -aG docker ec2-user
    curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    git clone https://github.com/jayjuhoonchoi/mining-equipment-monitor.git /home/ec2-user/app
    cd /home/ec2-user/app
    docker-compose up -d
  USERDATA

  tags = {
    Name = "mining-equipment-monitor"
  }
}

output "public_ip" {
  value = aws_instance.app_server.public_ip
}

output "ssh_command" {
  value = "ssh -i ~/.ssh/juhoon-key.pem ec2-user@${aws_instance.app_server.public_ip}"
}
