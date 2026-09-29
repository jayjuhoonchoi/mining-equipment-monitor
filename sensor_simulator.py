import random

def check_temperature(temp):
    if temp > 90:
        return "Warning"
    else:
        return "OK"

def check_vibration(vib):
    if vib > 8:
        return "Warning"
    else:
        return "OK"

def generate_readings():
    equipment_ids = ["CV-101", "PMP-07", "CV-102"]
    readings = []
    for eq_id in equipment_ids:
        temp = round(random.uniform(60, 95), 1)
        vib = round(random.uniform(2, 10), 1)
        readings.append({
            "equipment_id": eq_id,
            "temperature": temp,
            "vibration": vib
        })
    return readings