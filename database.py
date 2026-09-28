import psycopg2
import pandas as pd

def get_connection():
    return psycopg2.connect(dbname="postgres", user="juhoon")

def save_reading(cursor, equipment_id, temperature, status):
    cursor.execute(
        "INSERT INTO readings (equipment_id, temperature, status) VALUES (%s, %s, %s)",
        (equipment_id, temperature, status)
    )

def get_all_readings(conn):
    return pd.read_sql("SELECT * FROM readings", conn)