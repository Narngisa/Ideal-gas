from ideal_gas import PVnRT, PVgMRT, Pressure, Volume, Mole, Temperature, Gram, MolarMass

def test_calculate_pressure_PVnRT():
    gas = PVnRT(
        volume=Volume(volume=7600, unit="ml"),
        mole=Mole(mole=8, unit="mol"),
        temperature=Temperature(temperature=27, unit="C"),
    )

    expected = (8 * 0.0821 * (27 + 273)) / (7600 / 1000)
    assert gas.calculate_pressure == expected

def test_calculate_volume_PVnRT():
    gas = PVnRT(
        pressure=Pressure(pressure=1520, unit="mmHg"),
        mole=Mole(mole=7, unit="mol"),
        temperature=Temperature(temperature=298, unit="K"),
    )

    expected = (7 * 0.0821 * (298)) / (1520 / 760)
    assert gas.calculate_volume == expected

def test_calculate_mole_PVnRT():
    gas = PVnRT(
        pressure=Pressure(pressure=3800, unit="Torr"),
        volume=Volume(volume=7, unit="dm3"),
        temperature=Temperature(temperature=45, unit="C"),
    )

    expected = ((3800 / 760) * 7) / (0.0821 * (45 + 273))
    assert gas.calculate_mole == expected

def test_calculate_temperature_PVnRT():
    gas = PVnRT(
        pressure=Pressure(pressure=2, unit="atm"),
        volume=Volume(volume=41, unit="cm3"),
        mole=Mole(mole=21, unit="mol"),
    )

    expected = (2 * (41 / 1000)) / (0.0821 * 21)
    assert gas.calculate_temperature == expected

def test_calculate_pressure_PVgMRT():
    gas = PVgMRT(
        volume=Volume(volume=3, unit="L"),
        gram=Gram(gram=4, unit="kg"),
        molar_mass=MolarMass(molar_mass=8, unit="g/mol"),
        temperature=Temperature(temperature=45, unit="C")
    )

    expected = (((4 * 1000) / 8) * 0.0821 * (45 + 273)) / 3
    assert gas.calculate_pressure == expected

def test_calculate_volume_PVgMRT():
    gas = PVgMRT(
        pressure=Pressure(pressure=760, unit="mmHg"),
        gram=Gram(gram=20, unit="g"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol"),
        temperature=Temperature(temperature=300, unit="K")
    )

    expected = ((20 / 3) * 0.0821 * 300) / (760 / 760)
    assert gas.calculate_volume == expected

def test_calculate_gram_PVgMRT():
    gas = PVgMRT(
        pressure=Pressure(pressure=760, unit="mmHg"),
        volume=Volume(volume=20, unit="dm3"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol"),
        temperature=Temperature(temperature=300, unit="K")
    )

    expected = ((760 / 760) * 20 * 3) / (0.0821 * 300)
    assert gas.calculate_gram == expected

def test_calculate_molar_mass_PVgMRT():
    gas = PVgMRT(
        pressure=Pressure(pressure=1520, unit="Torr"),
        volume=Volume(volume=20, unit="ml"),
        gram=Gram(gram=6, unit="kg"),
        temperature=Temperature(temperature=25, unit="C")
    )

    expected = ((6 * 1000) * 0.0821 * (25 + 273)) / ((1520 / 760) * (20 / 1000))
    assert gas.calculate_molar_mass == expected

def test_calculate_temperature_PVgMRT():
    gas = PVgMRT(
        pressure=Pressure(pressure=12, unit="atm"),
        volume=Volume(volume=30, unit="cm3"),
        gram=Gram(gram=20, unit="g"),
        molar_mass=MolarMass(molar_mass=3, unit="g/mol")
    )

    expected = (12 * (30 / 1000) * 3) / (20 * 0.0821)
    assert gas.calculate_temperature == expected
