import logging
from logger_setup import setup_logging
from sensor_simulator import generate_readings, check_temperature, check_vibration
from database import get_connection, save_reading, get_all_readings
from analysis import get_average, get_max

setup_logging()

logging.info("Starting sensor check")

conn = get_connection()
cursor = conn.cursor()

readings = generate_readings()

for r in readings:
    temp_status = check_temperature(r["temperature"])
    vib_status = check_vibration(r["vibration"])

    if temp_status == "Warning":
        logging.warning(f"{r['equipment_id']}: high temperature detected: {r['temperature']}")
    if vib_status == "Warning":
        logging.warning(f"{r['equipment_id']}: high vibration detected: {r['vibration']}")

    overall_status = "Warning" if temp_status == "Warning" or vib_status == "Warning" else "OK"
    save_reading(cursor, r["equipment_id"], r["temperature"], r["vibration"], overall_status)

conn.commit()
logging.info("All readings saved to database")

df = get_all_readings(conn)
print("Average temperature:", get_average(df))
print("Max temperature:", get_max(df))