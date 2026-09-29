import os
import psycopg2
import pandas as pd

def get_connection():
    return psycopg2.connect(
        dbname=os.environ.get("DB_NAME", "postgres"),
        user=os.environ.get("DB_USER", "juhoon"),
        password=os.environ.get("DB_PASSWORD", ""),
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", "5432")
    )

def save_reading(cursor, equipment_id, temperature, vibration, status):
    cursor.execute(
        "INSERT INTO readings (equipment_id, temperature, vibration, status) VALUES (%s, %s, %s, %s)",
        (equipment_id, temperature, vibration, status)
    )

def get_all_readings(conn):
    return pd.read_sql("SELECT * FROM readings", conn)