from ideal_gas import PVnRT, Pressure, Volume, Mole, Temperature

def test_calculate_pressure():
    gas = PVnRT(
        volume=Volume(volume=7600, unit="ml"),
        mole=Mole(mole=8, unit="mol"),
        temperature=Temperature(temperature=27, unit="C"),
    )

    expected = (8 * 0.0821 * (27 + 273)) / (7600 / 1000)
    assert gas.calculate_pressure == expected

def test_calculate_volume():
    gas = PVnRT(
        pressure=Pressure(pressure=1520, unit="mmHg"),
        mole=Mole(mole=7, unit="mol"),
        temperature=Temperature(temperature=298, unit="K"),
    )

    expected = (7 * 0.0821 * (298)) / (1520 / 760)
    assert gas.calculate_volume == expected

def test_calculate_mole():
    gas = PVnRT(
        pressure=Pressure(pressure=3800, unit="Torr"),
        volume=Volume(volume=7, unit="dm3"),
        temperature=Temperature(temperature=45, unit="C"),
    )

    expected = ((3800 / 760) * 7) / (0.0821 * (45 + 273))
    assert gas.calculate_mole == expected

def test_calculate_temperature():
    gas = PVnRT(
        pressure=Pressure(pressure=2, unit="atm"),
        volume=Volume(volume=41, unit="cm3"),
        mole=Mole(mole=21, unit="mol"),
    )

    expected = (2 * (41 / 1000)) / (0.0821 * 21)
    assert gas.calculate_temperature == expected
