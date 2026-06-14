from ideal_gas import PVnRT, PVgMRT, Pressure, Volume, Mole, Temperature, Gram, MolarMass
import pytest

def test_raise_pressure_exits():
    gas_PV_nRT = PVnRT(pressure=Pressure(pressure=1, unit="atm"))
    gas_PV_gMRT = PVgMRT(pressure=Pressure(pressure=1, unit="atm"))

    with pytest.raises(ValueError, match="pressure already exists"):
        gas_PV_nRT.calculate_pressure
        gas_PV_gMRT.calculate_pressure

def test_raise_volume_exits():
    gas_PV_nRT = PVnRT(volume=Volume(volume=1000, unit="cm3"))
    gas_PV_gMRT = PVgMRT(volume=Volume(volume=1000, unit="cm3"))

    with pytest.raises(ValueError, match="volume already exists"):
        gas_PV_nRT.calculate_volume
        gas_PV_gMRT.calculate_volume

def test_raise_mole_exits():
    gas_PV_nRT = PVnRT(mole=Mole(mole=15, unit="mol"))

    with pytest.raises(ValueError, match="mole already exists"):
        gas_PV_nRT.calculate_mole

def test_raise_temperature_exits():
    gas_PV_nRT = PVnRT(temperature=Temperature(temperature=300, unit="K"))
    gas_PV_gMRT = PVgMRT(temperature=Temperature(temperature=300, unit="K"))

    with pytest.raises(ValueError, match="temperature already exists"):
        gas_PV_nRT.calculate_temperature
        gas_PV_gMRT.calculate_temperature

def test_raise_gram_exits():
    gas_PV_gMRT = PVgMRT(gram=Gram(gram=10, unit="g"))

    with pytest.raises(ValueError, match="gram already exists"):
        gas_PV_gMRT.calculate_gram

def test_raise_molar_mass_exits():
    gas_PV_gMRT = PVgMRT(molar_mass=MolarMass(molar_mass=10, unit="g/mol"))

    with pytest.raises(ValueError, match="molar mass already exists"):
        gas_PV_gMRT.calculate_molar_mass
