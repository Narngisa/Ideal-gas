from ideal_gas import Pressure, Volume, Mole, Temperature
import pytest

@pytest.mark.parametrize("value, unit, expected",[
        (760, "Torr", 1),
        (1520, "mmHg", 2),
        (1, "atm", 1),
    ]
)

def test_pressure_conversion(value, unit, expected):
    p = Pressure(pressure=value, unit=unit)
    assert p._atmosphere == expected

@pytest.mark.parametrize("value, unit, expected", [
    (1200, "cm3", 1.2),
    (5000, "ml", 5),
    (8, "L", 8),
    (7.4, "dm3", 7.4)
])

def test_volume_conversion(value, unit, expected):
    v = Volume(volume=value, unit=unit)
    assert v._liter == expected

@pytest.mark.parametrize("value, unit, expected", [
    (7, "mol", 7)
])

def test_mole_conversion(value, unit, expected):
    v = Mole(mole=value, unit=unit)
    assert v._mol == expected

@pytest.mark.parametrize("value, unit, expected", [
    (27, "C", 300),
    (225, "K", 225)
])

def test_temperature_conversion(value, unit, expected):
    v = Temperature(temperature=value, unit=unit)
    assert v._kelvin == expected
