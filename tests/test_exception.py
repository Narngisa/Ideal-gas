from ideal_gas import PVnRT, Pressure, Volume, Mole, Temperature
import pytest

def test_calculate_raise_pressure_exits():
    gas = PVnRT(pressure=Pressure(pressure=1, unit="atm"))

    with pytest.raises(ValueError, match="pressure already exists"):
        gas.calculate_pressure

def test_calculate_raise_volume_exits():
    gas = PVnRT(volume=Volume(volume=1000, unit="cm3"))

    with pytest.raises(ValueError, match="volume already exists"):
        gas.calculate_volume

def test_calculate_raise_mole_exits():
    gas = PVnRT(mole=Mole(mole=15, unit="mol"))

    with pytest.raises(ValueError, match="mole already exists"):
        gas.calculate_mole

def test_calculate_raise_temperature_exits():
    gas = PVnRT(temperature=Temperature(temperature=25, unit="C"))

    with pytest.raises(ValueError, match="temperature already exists"):
        gas.calculate_temperature
