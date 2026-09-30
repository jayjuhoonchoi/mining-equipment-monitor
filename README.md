# Mining Equipment Monitor

A small monitoring pipeline for mining equipment (conveyors, pumps).
It simulates sensor readings, classifies each reading, logs warnings,
stores everything in PostgreSQL, and reports summary statistics.

Built as a learning project to connect field experience in Australian
mining with IT, data and industrial technology skills.

## Architecture

    sensor simulator -> validation/classification -> PostgreSQL -> analysis
                                 |
                              logging

## Project structure

| File | Responsibility |
|---|---|
| `main.py` | Runs the whole pipeline in order |
| `sensor_simulator.py` | Generates readings, classifies them (OK / Warning) |
| `database.py` | PostgreSQL connection, save and query functions |
| `analysis.py` | Average and max using pandas |
| `logger_setup.py` | Central logging configuration |

## Requirements

- Python 3.10+
- PostgreSQL
- `pip install psycopg2-binary pandas`

## Setup

    psql postgres -c "CREATE TABLE readings (
        id SERIAL PRIMARY KEY,
        equipment_id TEXT,
        temperature FLOAT,
        status TEXT
    );"

## Run

    python3 main.py

## Roadmap

- [x] Sensor simulation, PostgreSQL storage, analysis
- [x] Equipment IDs, vibration readings, per-metric classification
- [ ] REST API (FastAPI)
- [ ] Docker Compose
- [ ] Tests and CI (GitHub Actions)
- [ ] MQTT telemetry
- [ ] Industrial architecture notes (PLC, SCADA, Modbus, OPC UA)
- [ ] AWS deployment with Terraform


![tests](https://github.com/jayjuhoonchoi/mining-equipment-monitor/actions/workflows/test.yml/badge.svg)