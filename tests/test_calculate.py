from ideal_gas import PVnRT, PVgMRT, Pressure, Volume, Mole, Temperature, Gram, MolarMass

def test_calculate_pressure():
    gas_PVnRT = PVnRT(
        volume=Volume(volume=7600, unit="ml"),
        mole=Mole(mole=8, unit="mol"),
        temperature=Temperature(temperature=27, unit="C"),
    )

    expected_PVnRT = (8 * 0.0821 * (27 + 273)) / (7600 / 1000)
    assert abs(gas_PVnRT.calculate_pressure - expected_PVnRT) < 1e-9

    gas_PVgMRT = PVgMRT(
        volume=Volume(volume=3, unit="L"),
        gram=Gram(gram=4, unit="kg"),
        molar_mass=MolarMass(molar_mass=8, unit="g/mol"),
        temperature=Temperature(temperature=45, unit="C")
    )

    expected_PVgMRT = (((4 * 1000) / 8) * 0.0821 * (45 + 273)) / 3
    assert abs(gas_PVgMRT.calculate_pressure - expected_PVgMRT) < 1e-9

def test_calculate_volume():
    gas_PVnRT = PVnRT(
        pressure=Pressure(pressure=1520, unit="mmHg"),
        mole=Mole(mole=7, unit="mol"),
        temperature=Temperature(temperature=298, unit="K"),
    )

    expected_PVnRT = (7 * 0.0821 * (298)) / (1520 / 760)
    assert abs(gas_PVnRT.calculate_volume - expected_PVnRT) < 1e-9

    gas_PVgMRT = PVgMRT(
        pressure=Pressure(pressure=760, unit="mmHg"),
        gram=Gram(gram=20, unit="g"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol"),
        temperature=Temperature(temperature=300, unit="K")
    )

    expected_PVgMRT = ((20 / 3) * 0.0821 * 300) / (760 / 760)
    assert abs(gas_PVgMRT.calculate_volume - expected_PVgMRT) < 1e-9

def test_calculate_mole():
    gas_PVnRT = PVnRT(
        pressure=Pressure(pressure=3800, unit="Torr"),
        volume=Volume(volume=7, unit="dm3"),
        temperature=Temperature(temperature=45, unit="C"),
    )

    expected_PVnRT = ((3800 / 760) * 7) / (0.0821 * (45 + 273))
    assert abs(gas_PVnRT.calculate_mole - expected_PVnRT) < 1e-9

def test_calculate_temperature():
    gas_PVnRT = PVnRT(
        pressure=Pressure(pressure=2, unit="atm"),
        volume=Volume(volume=41, unit="cm3"),
        mole=Mole(mole=21, unit="mol"),
    )

    expected_PVnRT = (2 * (41 / 1000)) / (0.0821 * 21)
    assert abs(gas_PVnRT.calculate_temperature - expected_PVnRT) < 1e-9

    gas_PVgMRT = PVgMRT(
        pressure=Pressure(pressure=12, unit="atm"),
        volume=Volume(volume=30, unit="cm3"),
        gram=Gram(gram=20, unit="g"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol")
    )

    expected_PVgMRT = (12 * (30 / 1000) * 3) / (20 * 0.0821)
    assert abs(gas_PVgMRT.calculate_temperature - expected_PVgMRT) < 1e-9

def test_calculate_gram():
    gas_PVgMRT = PVgMRT(
        pressure=Pressure(pressure=760, unit="mmHg"),
        volume=Volume(volume=20, unit="dm3"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol"),
        temperature=Temperature(temperature=300, unit="K")
    )

    expected_PVgMRT = ((760 / 760) * 20 * 3) / (0.0821 * 300)
    assert abs(gas_PVgMRT.calculate_gram - expected_PVgMRT) < 1e-9

def test_calculate_molar_mass():
    gas_PVgMRT = PVgMRT(
        pressure=Pressure(pressure=1520, unit="Torr"),
        volume=Volume(volume=20, unit="ml"),
        gram=Gram(gram=6, unit="kg"),
        temperature=Temperature(temperature=25, unit="C")
    )

    expected_PVgMRT = ((6 * 1000) * 0.0821 * (25 + 273)) / ((1520 / 760) * (20 / 1000))
    assert abs(gas_PVgMRT.calculate_molar_mass - expected_PVgMRT) < 1e-9
