import subprocess
import csv

def check_device(ip):
    result = subprocess.run(['ping', '-c', '1', ip], capture_output=True, text=True)
    if result.returncode == 0:
        return "Online"
    else:
        return "Offline"

devices = ["8.8.8.8", "1.1.1.1", "192.0.2.1"]

results = []

for ip in devices:
    status = check_device(ip)
    print(ip, "-", status)
    results.append({"ip": ip, "status": status})

with open("network_report.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["ip", "status"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("Saved to network_report.csv")