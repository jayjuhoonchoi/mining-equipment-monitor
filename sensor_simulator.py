import random

def check_temperature(temp):
    if temp > 90:
        return "Warning"
    else:
        return "OK"

def generate_readings(count):
    readings = []
    for i in range(count):
        readings.append(round(random.uniform(60, 95), 1))
    return readings