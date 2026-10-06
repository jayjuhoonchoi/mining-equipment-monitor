import csv
import random

def generate_temperature():
    readings = []
    for i in range(3):
        temperature = round(random.uniform(60, 110), 1)
        readings.append(temperature)
    return readings

def check_temperature(temperature):
    if temperature > 90:
        return "Warning"
    else:
        return "OK"

def save_report(results, filename):
    with open(filename, "w")as file:
        writer = csv.DictWriter(file, fieldnames=["temperature", "status"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

temperatures = generate_temperature()
print(temperatures)

results = []
ok_count = 0

for t in temperatures:
    status = check_temperature(t)
    print(t, "-", status)
    results.append({"temperature": t, "status": status})
    if status == "OK":
        ok_count = ok_count + 1

save_report(results, "temperature_report.csv")
print("Saved to temperature_report.csv")
print("number of OK temperatures:", ok_count)