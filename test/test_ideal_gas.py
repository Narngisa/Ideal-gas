from ideal_gas import Unit
import pytest

@pytest.mark.parametrize("value, unit, expected",[
        (760, "Torr", 1),
        (1520, "mmHg", 2),
        (1, "atm", 1),
    ]
)

def test_pressure_conversion(value, unit, expected):
    p = Unit.pressure(pressure=value, unit=unit)
    assert p._atmosphere == expected
