from ideal_gas import PVnRT, Pressure, Volume, Mole, Temperature
import pytest

def test_calculate_pressure_missing_data():
    gas = PVnRT(mole=Mole(mole=2, unit="mol"))

    with pytest.raises(ValueError, match="volume, mole, and temperature are required"):
        gas.calculate_pressure

def test_calculate_volume_missing_data():
    gas = PVnRT(pressure=Pressure(pressure=2, unit="Torr"))

    with pytest.raises(ValueError, match="pressure, mole, and temperature are required"):
        gas.calculate_volume

def test_calculate_mole_missing_data():
    gas = PVnRT(temperature=Temperature(temperature=25, unit="C"))

    with pytest.raises(ValueError, match="pressure, volume, and temperature are required"):
        gas.calculate_mole

def test_calculate_temperature_missing_data():
    gas = PVnRT(volume=Volume(volume=25, unit="cm3"))

    with pytest.raises(ValueError, match="pressure, volume, and mole are required"):
        gas.calculate_temperature
