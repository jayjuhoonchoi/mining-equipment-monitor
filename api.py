from fastapi import FastAPI
from database import get_connection, get_all_readings

app = FastAPI()

@app.get("/readings")
def read_all():
    conn = get_connection()
    df = get_all_readings(conn)
    df = df.dropna()
    return df.to_dict(orient="records")