# Mining Equipment Monitor

![tests](https://github.com/jayjuhoonchoi/mining-equipment-monitor/actions/workflows/test.yml/badge.svg)

An equipment monitoring pipeline for mining sites (conveyors, pumps). It simulates sensor telemetry, classifies readings, stores them in PostgreSQL, serves them over a REST API, and ships as a containerized, tested, infrastructure-as-code project.

Built to connect field experience in Australian mining with IT, data engineering and industrial technology skills.

## Architecture

sensor simulator -> MQTT broker -> subscriber -> PostgreSQL -> analysis / API
|
logging

## Project structure

| File | Responsibility |
|---|---|
| `main.py` | Runs the sensor to classify to store pipeline |
| `sensor_simulator.py` | Generates readings, classifies them (OK / Warning) |
| `database.py` | PostgreSQL connection, save and query functions |
| `analysis.py` | Average and max using pandas |
| `api.py` | FastAPI endpoint serving stored readings |
| `mqtt_publisher.py` / `mqtt_subscriber.py` | MQTT telemetry simulation |
| `logger_setup.py` | Central logging configuration |
| `test_sensor_simulator.py` | pytest unit tests |
| `Dockerfile` / `docker-compose.yml` | Containerized app and PostgreSQL |
| `main.tf` | Terraform-managed S3 bucket (tested against LocalStack) |

## Run with Docker (recommended)

```bash
docker compose up --build
```

API available at `http://localhost:8080/readings`.

## Run locally

```bash
pip install -r requirements.txt
psql postgres -c "CREATE TABLE readings (
    id SERIAL PRIMARY KEY,
    equipment_id TEXT,
    temperature FLOAT,
    vibration FLOAT,
    status TEXT
);"
python3 main.py
```

## Tests

```bash
pytest
```

## Industrial context

This project mirrors a small slice of a mining site's monitoring stack:

- **PLC**: a small industrial computer attached to one piece of equipment, making immediate decisions (e.g. shut down if temperature exceeds a limit). `check_temperature()` mirrors this logic in software.
- **SCADA**: collects data from many PLCs into one view. `main.py` and `analysis.py` play this role here.
- **HMI**: the screen operators look at. The `/readings` API endpoint is a step toward one.
- **Modbus TCP / OPC UA**: real industrial protocols between PLCs and SCADA. This project uses **MQTT** instead, the modern, IT-friendly equivalent increasingly used in smart-factory setups.
- **Historian**: a database storing equipment history over time. PostgreSQL plays that role here.

## Infrastructure as code

`main.tf` provisions an S3 bucket via Terraform, tested against LocalStack (free tier) to avoid AWS costs during development.

```bash
terraform init
terraform plan
terraform apply
```

To deploy against real AWS: remove the `endpoints` block and `skip_*` flags from the provider configuration, and configure real AWS credentials.

## Roadmap

- [x] Sensor simulation, PostgreSQL storage, analysis
- [x] Equipment IDs, vibration readings, per-metric classification
- [x] REST API (FastAPI)
- [x] Docker Compose
- [x] Tests and CI (GitHub Actions)
- [x] MQTT telemetry
- [x] Industrial architecture notes (PLC, SCADA, Modbus, OPC UA)
- [x] Infrastructure as code (Terraform, tested via LocalStack)
- [ ] AWS deployment with real infrastructure


## PLC Ladder Logic (Learning Log)

Practiced PLC ladder logic fundamentals using [PLCFiddle](https://www.plcfiddle.com/) (Code School track):

- NO/NC contact behavior and fail-safe design (NC for Stop/alarm circuits)
- Self-holding (seal-in) circuits
- AND + OR combined logic

**Saved fiddle:** [AND+OR combined logic exercise](https://www.plcfiddle.com/fiddles?v=2&d=eJyVkDFvwjAQhf9K9eYb7IQ4wXsHJqQOXSIPhrgUKXFQcBAV8n-vzlEhaoaWxfKdvnf37t1wscPR7lp3hr5BZvxebDs66A_bnh0hfJ0cNHZ934LgbcfVxp_G8CIRCTJ_SpMljfqnZjuGx6LyOVGGGAnD6A_TbdB1QRUpQ1hB12uSmSEU0LWUhqD4IwxBCiEEdG0iwbWucz6kAcW0fopr00BzXHcL1-OeTaolpB5QHxxD1RLKF5PWDP3cN1i__wShtU3jhnSJYn9SzCgW0sIhU_IPKk9UNqPY6W-qTIHeLUhaGULngmWdd9fwOqXFtMwptd5nE2Q19d5Gf-C6jPEbjD7A_w)