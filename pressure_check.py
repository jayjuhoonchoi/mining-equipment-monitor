import random

def generate_pressures():
    readings = []
    for i in range(5):
        pressure = round(random.uniform(80, 120), 1)
        readings.append(pressure)
    return readings

pressures = generate_pressures()
print(pressures)

def check_pressure(pressures):
    if pressures > 100:
        return "Warning"
    else:
        return "OK"

for p in pressures:
    status = check_pressure(p)
    print(p, "-", status)

