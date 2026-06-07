from ideal_gas import PVnRT, Unit
import pytest

@pytest.mark.parametrize("value, unit, expected",[
        (760, "Torr", 1),
        (1520, "mmHg", 2),
        (1, "atm", 1),
    ]
)

def test_pressure_conversion(value, unit, expected):
    p = Unit.Pressure(pressure=value, unit=unit)
    assert p._atmosphere == expected

@pytest.mark.parametrize("value, unit, expected", [
    (1200, "cm3", 1.2),
    (5000, "ml", 5),
    (8, "L", 8),
    (7.4, "dm3", 7.4)
])

def test_volume_conversion(value, unit, expected):
    v = Unit.Volume(volume=value, unit=unit)
    assert v._liter == expected

@pytest.mark.parametrize("value, unit, expected", [
    (7, "mol", 7)
])

def test_mole_conversion(value, unit, expected):
    v = Unit.Mole(mole=value, unit=unit)
    assert v._mol == expected

@pytest.mark.parametrize("value, unit, expected", [
    (27, "C", 300),
    (225, "K", 225)
])

def test_temperature_conversion(value, unit, expected):
    v = Unit.Temperature(temperature=value, unit=unit)
    assert v._kelvin == expected

def test_calculate_pressure():
    gas = PVnRT(
        volume=Unit.Volume(volume=7600, unit="ml"),
        mole=Unit.Mole(mole=8, unit="mol"),
        temperature=Unit.Temperature(temperature=27, unit="C"),
    )

    expected = (8 * 0.0821 * (27 + 273)) / (7600 / 1000)
    assert gas.calculate_pressure == expected
