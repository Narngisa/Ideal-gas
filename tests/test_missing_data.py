from ideal_gas import PMRT, Density, Gram, MolarMass, Molarity, PVdRT, PVgMRT, PVnRT, Pressure, Volume, Mole, Temperature
import pytest

def test_pressure_missing_data():
    gas_PV_nRT = PVnRT(mole=Mole(mole=2, unit="mol"))
    with pytest.raises(ValueError, match="volume, mole, and temperature are required"):
        gas_PV_nRT.calculate_pressure

    gas_PV_gMRT = PVgMRT(volume=Volume(volume=700, unit="cm3"))
    with pytest.raises(ValueError, match="volume, gram, molar mass, and temperature are required"):
        gas_PV_gMRT.calculate_pressure

    gas_PV_dRT = PVdRT(density=Density(density=4, unit="g/L"))
    with pytest.raises(ValueError, match="volume, density, and temperature are required"):
        gas_PV_dRT.calculate_pressure

    gas_P_MRT = PMRT(temperature=Temperature(temperature=7, unit="C"))
    with pytest.raises(ValueError, match="molarity, and temperature are required"):
        gas_P_MRT.calculate_pressure

def test_volume_missing_data():
    gas_PV_nRT = PVnRT(pressure=Pressure(pressure=2, unit="Torr"))
    with pytest.raises(ValueError, match="pressure, mole, and temperature are required"):
        gas_PV_nRT.calculate_volume

    gas_PV_gMRT = PVgMRT(pressure=Pressure(pressure=4, unit="atm"))
    with pytest.raises(ValueError, match="pressure, gram, molar mass, and temperature are required"):
        gas_PV_gMRT.calculate_volume

    gas_PV_dRT = PVdRT(pressure=Pressure(pressure=760, unit="mmHg"))
    with pytest.raises(ValueError, match="pressure, density, and temperature are required"):
        gas_PV_dRT.calculate_volume

def test_mole_missing_data():
    gas_PV_nRT = PVnRT(temperature=Temperature(temperature=25, unit="C"))
    with pytest.raises(ValueError, match="pressure, volume, and temperature are required"):
        gas_PV_nRT.calculate_mole

def test_temperature_missing_data():
    gas_PV_nRT = PVnRT(volume=Volume(volume=25, unit="cm3"))
    with pytest.raises(ValueError, match="pressure, volume, and mole are required"):
        gas_PV_nRT.calculate_temperature

    gas_PV_gMRT = PVgMRT(gram=Gram(gram=30, unit="kg"))
    with pytest.raises(ValueError, match="pressure, volume, gram, and molar mass are required"):
        gas_PV_gMRT.calculate_temperature

    gas_PV_dRT = PVdRT(volume=Volume(volume=4, unit="L"))
    with pytest.raises(ValueError, match="pressure, volume, and density are required"):
        gas_PV_dRT.calculate_temperature

    gas_P_MRT = PMRT(molarity=Molarity(molarity=7, unit="mol/L"))
    with pytest.raises(ValueError, match="pressure, and molarity are required"):
        gas_P_MRT.calculate_temperature

def test_gram_missing_data():
    gas_PV_gMRT = PVgMRT(molar_mass=MolarMass(molar_mass=7, unit="g/mol"))
    with pytest.raises(ValueError, match="pressure, volume, molar mass, and temperature are required"):
        gas_PV_gMRT.calculate_gram

def test_molar_mass_missing_data():
    gas_PV_gMRT = PVgMRT(temperature=Temperature(temperature=25, unit="C"))
    with pytest.raises(ValueError, match="pressure, volume, gram, and temperature are required"):
        gas_PV_gMRT.calculate_molar_mass

def test_density_missing_data():
    gas_PV_dRT = PVdRT(temperature=Temperature(temperature=27, unit="C"))
    with pytest.raises(ValueError, match="pressure, volume, and temperature are required"):
        gas_PV_dRT.calculate_density

def test_malarity_missing_data():
    gas_P_MRT = PMRT(pressure=Pressure(pressure=25, unit="atm"))
    with pytest.raises(ValueError, match="pressure, and temperature are required"):
        gas_P_MRT.calculate_molarity
