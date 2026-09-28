import logging
from logger_setup import setup_logging
from sensor_simulator import generate_readings, check_temperature
from database import get_connection, save_reading, get_all_readings
from analysis import get_average, get_max

setup_logging()

logging.info("Starting sensor check")

conn = get_connection()
cursor = conn.cursor()

temperatures = generate_readings(5)

for temp in temperatures:
    status = check_temperature(temp)
    if status == "Warning":
        logging.warning(f"High temperature detected: {temp}")
    save_reading(cursor, "AUTO-CHECK", temp, status)

conn.commit()
logging.info("All readings saved to database")

df = get_all_readings(conn)
print("Average:", get_average(df))
print("Max:", get_max(df))