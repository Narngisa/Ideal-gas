from ideal_gas import Pressure, Volume, Mole, Temperature
import pytest

@pytest.mark.parametrize("value, unit, expected",[
        (760, "Torr", 1),
        (760, "mmHg", 1),
        (1, "atm", 1),
    ]
)

def test_pressure_conversion(value, unit, expected):
    p = Pressure(pressure=value, unit=unit)
    assert p.atmosphere == expected

def test_pressure_zero():
    with pytest.raises(ValueError, match="Pressure must be greater than zero"):
        Pressure(pressure=0, unit="atm")
        Pressure(pressure=0, unit="Torr")
        Pressure(pressure=0, unit="mmHg")

@pytest.mark.parametrize("value, unit, expected", [
    (1000, "cm3", 1),
    (1000, "ml", 1),
    (1, "L", 1),
    (1, "dm3", 1)
])

def test_volume_conversion(value, unit, expected):
    v = Volume(volume=value, unit=unit)
    assert v.liter == expected

def test_volume_zero():
    with pytest.raises(ValueError, match="Volume must be greater than zero"):
        Volume(volume=0, unit="L")
        Volume(volume=0, unit="dm3")
        Volume(volume=0, unit="cm3")
        Volume(volume=0, unit="ml")

@pytest.mark.parametrize("value, unit, expected", [
    (1, "mol", 1)
])

def test_mole_conversion(value, unit, expected):
    v = Mole(mole=value, unit=unit)
    assert v.mol == expected

def test_mole_zero():
    with pytest.raises(ValueError, match="Mole must be greater than zero"):
        Mole(mole=0, unit="mol")

@pytest.mark.parametrize("value, unit, expected", [
    (27, "C", 300),
    (0, "C", 273),
    (273, "K", 273)
])

def test_temperature_conversion(value, unit, expected):
    v = Temperature(temperature=value, unit=unit)
    assert v.kelvin == expected

def test_temperature_kelvin_zero():
    with pytest.raises(ValueError, match="Temperature must be greater than zero"):
        Temperature(temperature=-273, unit="C")

def test_temperature_above_absolute_zero():
    t = Temperature(temperature=-272, unit="C")
    assert t.kelvin == 1
