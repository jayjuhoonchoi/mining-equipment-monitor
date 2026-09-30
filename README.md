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
- [x] REST API (FastAPI)
- [x] Docker Compose
- [x] Tests and CI (GitHub Actions)
- [x] MQTT telemetry
- [ ] Industrial architecture notes (PLC, SCADA, Modbus, OPC UA)
- [ ] AWS deployment with Terraform


![tests](https://github.com/jayjuhoonchoi/mining-equipment-monitor/actions/workflows/test.yml/badge.svg)




## Industrial context

This project simulates a small slice of a mining site's monitoring stack.

- **PLC** (Programmable Logic Controller): a small industrial computer next
  to the equipment that makes immediate decisions (e.g. shut down if
  temperature exceeds a limit). `check_temperature()` mirrors this logic
  in software.
- **SCADA**: software that gathers data from many PLCs into one view.
  `main.py` and `analysis.py` play this role here.
- **HMI** (Human-Machine Interface): the screen operators look at.
  The `/readings` API endpoint is a first step toward one.
- **Modbus TCP / OPC UA**: real industrial communication protocols
  between PLCs and SCADA systems. This project uses **MQTT** instead,
  which is the modern, IT-friendly equivalent increasingly used in
  smart-factory setups.
- **Historian**: a database that stores equipment history over time.
  PostgreSQL plays that role here.