import random
import csv

def generate_pressures():
    readings = []
    for i in range(5):
        pressure = round(random.uniform(80, 120), 1)
        readings.append(pressure)
    return readings

def check_pressure(pressure):
    if pressure > 100:
        return "Warning"
    else:
        return "OK"

def save_report(results, filename):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["pressure", "status"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

pressures = generate_pressures()
print(pressures)

results = []

for p in pressures:
    status = check_pressure(p)
    print(p, "-", status)
    results.append({"pressure": p, "status": status})

save_report(results, "pressure_report.csv")
print("Saved to pressure_report.csv")


results = []
danger_count = 0

for p in pressures:
    status = check_pressure(p)
    print(p, "-", status)
    results.append({"pressure": p, "status": status})
    if status == "Warning":
        danger_count = danger_count + 1

print("위험한 펌프 개수:", danger_count)