from sensor_simulator import check_temperature, check_vibration

def test_check_temperature_warning():
    assert check_temperature(95) == "Warning"

def test_check_temperature_ok():
    assert check_temperature(80) == "OK"

def test_check_vibration_warning():
    assert check_vibration(9) == "Warning"

def test_check_vibration_ok():
    assert check_vibration(5) == "OK"