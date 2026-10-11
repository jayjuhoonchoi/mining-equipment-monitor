import subprocess
import csv

def check_device(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-t", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        return "Online"
    else:
        return "Offline"

def save_report(results, filename):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["ip", "status"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

if __name__ == "__main__":
    devices = ["8.8.8.8", "1.1.1.1", "192.168.0.1"]
    results = []

    for ip in devices:
        status = check_device(ip)
        print(ip, "-", status)
        results.append({"ip": ip, "status": status})

    save_report(results, "network_report.csv")
    print("Saved to network_report.csv")
