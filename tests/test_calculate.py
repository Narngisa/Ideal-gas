from ideal_gas import PMRT, Density, Molarity, PVdRT, PVnRT, PVgMRT, Pressure, Volume, Mole, Temperature, Gram, MolarMass

gas_constant = 0.0821
kelvin = 273

def test_calculate_pressure():
    gas_PV_nRT = PVnRT(
        volume=Volume(volume=7600, unit="ml"),
        mole=Mole(mole=8, unit="mol"),
        temperature=Temperature(temperature=27, unit="C"),
    )

    expected_PV_nRT = (8 * gas_constant * (27 + kelvin)) / (7600 / 1000)
    assert abs(gas_PV_nRT.calculate_pressure - expected_PV_nRT) < 1e-12

    gas_PV_gMRT = PVgMRT(
        volume=Volume(volume=3, unit="L"),
        gram=Gram(gram=4, unit="kg"),
        molar_mass=MolarMass(molar_mass=8, unit="g/mol"),
        temperature=Temperature(temperature=45, unit="C")
    )

    expected_PV_gMRT = (((4 * 1000) / 8) * gas_constant * (45 + kelvin)) / 3
    assert abs(gas_PV_gMRT.calculate_pressure - expected_PV_gMRT) < 1e-12

    gas_PV_dRT = PVdRT(
        volume=Volume(volume=12, unit="L"),
        density=Density(density=5, unit="g/L"),
        temperature=Temperature(temperature=330, unit="K")
    )

    expected_PV_dRT = (5 * gas_constant * 330) / 12
    assert abs(gas_PV_dRT.calculate_pressure - expected_PV_dRT) < 1e-12

    gas_P_MRT = PMRT(
        molarity=Molarity(molarity=8, unit="mol/L"),
        temperature=Temperature(temperature=277, unit="K")
    )

    expected_P_MRT = (8 * gas_constant * 277)
    assert abs(gas_P_MRT.calculate_pressure - expected_P_MRT) < 1e-12

def test_calculate_volume():
    gas_PV_nRT = PVnRT(
        pressure=Pressure(pressure=1520, unit="mmHg"),
        mole=Mole(mole=7, unit="mol"),
        temperature=Temperature(temperature=298, unit="K"),
    )

    expected_PV_nRT = (7 * gas_constant * (298)) / (1520 / 760)
    assert abs(gas_PV_nRT.calculate_volume - expected_PV_nRT) < 1e-12

    gas_PV_gMRT = PVgMRT(
        pressure=Pressure(pressure=760, unit="mmHg"),
        gram=Gram(gram=20, unit="g"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol"),
        temperature=Temperature(temperature=300, unit="K")
    )

    expected_PV_gMRT = ((20 / 3) * gas_constant * 300) / (760 / 760)
    assert abs(gas_PV_gMRT.calculate_volume - expected_PV_gMRT) < 1e-12

    gas_PV_dRT = PVdRT(
        pressure=Pressure(pressure=6, unit="atm"),
        density=Density(density=8, unit="g/L"),
        temperature=Temperature(temperature=325, unit="K")
    )

    expected_PV_dRT = (8 * gas_constant * 325) / 6
    assert abs(gas_PV_dRT.calculate_volume - expected_PV_dRT) < 1e-12

def test_calculate_mole():
    gas_PV_nRT = PVnRT(
        pressure=Pressure(pressure=3800, unit="Torr"),
        volume=Volume(volume=7, unit="dm3"),
        temperature=Temperature(temperature=45, unit="C"),
    )

    expected_PV_nRT = ((3800 / 760) * 7) / (gas_constant * (45 + kelvin))
    assert abs(gas_PV_nRT.calculate_mole - expected_PV_nRT) < 1e-12

def test_calculate_temperature():
    gas_PV_nRT = PVnRT(
        pressure=Pressure(pressure=2, unit="atm"),
        volume=Volume(volume=41, unit="cm3"),
        mole=Mole(mole=21, unit="mol"),
    )

    expected_PV_nRT = (2 * (41 / 1000)) / (gas_constant * 21)
    assert abs(gas_PV_nRT.calculate_temperature - expected_PV_nRT) < 1e-12

    gas_PV_gMRT = PVgMRT(
        pressure=Pressure(pressure=12, unit="atm"),
        volume=Volume(volume=30, unit="cm3"),
        gram=Gram(gram=20, unit="g"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol")
    )

    expected_PV_gMRT = (12 * (30 / 1000) * 3) / (20 * gas_constant)
    assert abs(gas_PV_gMRT.calculate_temperature - expected_PV_gMRT) < 1e-12

    gas_PV_dRT = PVdRT(
        pressure=Pressure(pressure=760, unit="Torr"),
        volume=Volume(volume=17, unit="L"),
        density=Density(density=8, unit="g/L"),
    )

    expected_PV_dRT = ((760 / 760) * 17) / (8 * gas_constant)
    assert abs(gas_PV_dRT.calculate_temperature - expected_PV_dRT) < 1e-12

    gas_P_MRT = PMRT(
        pressure=Pressure(pressure=1520, unit="Torr"),
        molarity=Molarity(molarity=8, unit="mol/L")
    )

    expected_P_MRT = ((1520 / 760) / (8 * gas_constant))
    assert abs(gas_P_MRT.calculate_temperature - expected_P_MRT) < 1e-12

def test_calculate_gram():
    gas_PV_gMRT = PVgMRT(
        pressure=Pressure(pressure=760, unit="mmHg"),
        volume=Volume(volume=20, unit="dm3"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol"),
        temperature=Temperature(temperature=300, unit="K")
    )

    expected_PV_gMRT = ((760 / 760) * 20 * 3) / (gas_constant * 300)
    assert abs(gas_PV_gMRT.calculate_gram - expected_PV_gMRT) < 1e-12

def test_calculate_molar_mass():
    gas_PV_gMRT = PVgMRT(
        pressure=Pressure(pressure=1520, unit="Torr"),
        volume=Volume(volume=20, unit="ml"),
        gram=Gram(gram=6, unit="kg"),
        temperature=Temperature(temperature=25, unit="C")
    )

    expected_PV_gMRT = ((6 * 1000) * gas_constant * (25 + kelvin)) / ((1520 / 760) * (20 / 1000))
    assert abs(gas_PV_gMRT.calculate_molar_mass - expected_PV_gMRT) < 1e-12

def test_calculate_density():
    gas_PV_dRT = PVdRT(
        pressure=Pressure(pressure=7, unit="atm"),
        volume=Volume(volume=100, unit="ml"),
        temperature=Temperature(temperature=27, unit="C")
    )

    expected_PV_dRT = (7 * (100 / 1000) / (gas_constant * (27 + kelvin)))
    assert abs(gas_PV_dRT.calculate_density - expected_PV_dRT) < 1e-12

def test_calculate_molariry():
    gas_P_MRT = PMRT(
        pressure=Pressure(pressure=1, unit="atm"),
        temperature=Temperature(temperature=25, unit="C")
    )

    expected_P_MRT = (1 / (gas_constant * (25 + kelvin)))
    assert abs(gas_P_MRT.calculate_molarity - expected_P_MRT) < 1e-12
