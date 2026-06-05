from dataclasses import KW_ONLY, dataclass
from typing import Optional
from units import _pressure, _volume, _mole, _temperature

gas_constant = 0.0821

@dataclass
class PVnRT:
    _: KW_ONLY
    pressure: Optional[_pressure] = None
    volume: Optional[_volume] = None
    mole: Optional[_mole] = None
    temperature: Optional[_temperature] = None

    @property
    def calculate_pressure(self):

        if self.pressure is not None:
            raise ValueError("pressure already exists")

        if (self.volume is None or self.mole is None or self.temperature is None):
            raise ValueError("volume, mole and temperature are required")

        return (self.mole._mol * gas_constant * self.temperature._kelvin) / self.volume._liter
