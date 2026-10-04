from network_check import save_report
import csv
import os

def test_save_report():
    results = [{"ip": "8.8.8.8", "status": "Online"}]
    save_report(results, "test_output.csv")

    with open("test_output.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert rows[0]["ip"] == "8.8.8.8"
    assert rows[0]["status"] == "Online"

    os.remove("test_output.csv")