from ideal_gas import Gram, MolarMass, PVgMRT, PVnRT, Pressure, Volume, Mole, Temperature
import pytest

def test_pressure_missing_data():
    gas_PVnRT = PVnRT(mole=Mole(mole=2, unit="mol"))
    with pytest.raises(ValueError, match="volume, mole, and temperature are required"):
        gas_PVnRT.calculate_pressure

    gas_PV_gMRT = PVgMRT(volume=Volume(volume=700, unit="cm3"))
    with pytest.raises(ValueError, match="volume, gram, molar mass, and temperature are required"):
        gas_PV_gMRT.calculate_pressure

def test_volume_missing_data():
    gas_PVnRT = PVnRT(pressure=Pressure(pressure=2, unit="Torr"))
    with pytest.raises(ValueError, match="pressure, mole, and temperature are required"):
        gas_PVnRT.calculate_volume

    gas_PV_gMRT = PVgMRT(pressure=Pressure(pressure=4, unit="atm"))
    with pytest.raises(ValueError, match="pressure, gram, molar mass, and temperature are required"):
        gas_PV_gMRT.calculate_volume

def test_mole_missing_data():
    gas_PVnRT = PVnRT(temperature=Temperature(temperature=25, unit="C"))
    with pytest.raises(ValueError, match="pressure, volume, and temperature are required"):
        gas_PVnRT.calculate_mole

def test_temperature_missing_data():
    gas_PVnRT = PVnRT(volume=Volume(volume=25, unit="cm3"))
    with pytest.raises(ValueError, match="pressure, volume, and mole are required"):
        gas_PVnRT.calculate_temperature

    gas_PV_gMRT = PVgMRT(gram=Gram(gram=30, unit="kg"))
    with pytest.raises(ValueError, match="pressure, volume, gram, and molar mass are required"):
        gas_PV_gMRT.calculate_temperature

def test_gram_missing_data():
    gas_PV_gMRT = PVgMRT(molar_mass=MolarMass(molar_mass=7, unit="g/mol"))
    with pytest.raises(ValueError, match="pressure, volume, molar mass, and temperature are required"):
        gas_PV_gMRT.calculate_gram

def test_molar_mass_missing_data():
    gas_PV_gMRT = PVgMRT(temperature=Temperature(temperature=25, unit="C"))
    with pytest.raises(ValueError, match="pressure, volume, gram, and temperature are required"):
        gas_PV_gMRT.calculate_molar_mass
