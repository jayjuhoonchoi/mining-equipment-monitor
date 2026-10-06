import csv
import random

def generate_vibrations():
    readings = []
    for i in range(4):
        vibration = round(random.uniform(0, 10), 1)
        readings.append(vibration)
    return readings

def check_vibration(vibration):
    if vibration > 8:
        return "Warning"
    else:
        return "OK"

def save_report(results, filename):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["vibration", "status"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

vibrations = generate_vibrations()
print(vibrations)

results = []

for v in vibrations:
    status = check_vibration(v)
    print(v, "-", status)
    results.append({"vibration": v, "status": status})

save_report(results, "vibration_report.csv")
print("Saved to vibration_report.csv")

results = []
ok_count = 0

for v in vibrations:
    status = check_vibration(v)
    print(v, "-", status)
    results.append({"vibration": v, "status": status})
    if status == "OK":
        ok_count = ok_count + 1

print("number of safe vibrations:", ok_count)