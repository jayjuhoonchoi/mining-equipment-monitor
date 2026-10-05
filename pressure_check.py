import random

def generate_pressures():
    readings = []
    for i in range(5):
        pressure = round(random.uniform(80, 120), 1)
        readings.append(pressure)
    return readings

pressures = generate_pressures()
print(pressures)