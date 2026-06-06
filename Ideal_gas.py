from dataclasses import KW_ONLY, dataclass
from typing import Optional, Literal

gas_constant = 0.0821

PressureUnit = Literal["atm", "Torr", "mmHg"]
VolumeUnit = Literal["ml", "cm3", "L", "dm3"]
MoleUnit = Literal["mol"]
TemperatureUnit = Literal["K", "C"]

@dataclass
class Unit:

    @dataclass
    class _pressure:
        _: KW_ONLY
        pressure: float
        unit: PressureUnit

        @property
        def _atmosphere(self) -> float:
            if self.unit == "atm":
                return self.pressure
            elif self.unit == "Torr" or self.unit == "mmHg":
                return self.pressure / 760
            raise ValueError(f"Unsupported pressure unit: {self.unit}")

    @dataclass
    class _volume:
        _: KW_ONLY
        volume: float
        unit: VolumeUnit

        @property
        def _liter(self) -> float:
            if self.unit == "L" or self.unit == "dm3":
                return self.volume
            elif self.unit == "ml" or self.unit == "cm3":
                return self.volume / 1000
            raise ValueError(f"Unsupported volume unit: {self.unit}")

    @dataclass
    class _mole:
        _: KW_ONLY
        mole: float
        unit: MoleUnit

        @property
        def _mol(self) -> float:
            if self.unit == "mol":
                return self.mole
            raise ValueError(f"Unsupported mole unit: {self.unit}")

    @dataclass
    class _temperature:
        _: KW_ONLY
        temperature: float
        unit: TemperatureUnit

        @property
        def _kelvin(self) -> float:
            if self.unit == "K":
                return self.temperature
            elif self.unit == "C":
                return self.temperature + 273
            raise ValueError(f"Unsupported temperature unit: {self.unit}")

@dataclass
class PVnRT:
    _: KW_ONLY
    pressure: Optional[Unit._pressure] = None
    volume: Optional[Unit._volume] = None
    mole: Optional[Unit._mole] = None
    temperature: Optional[Unit._temperature] = None

    @property
    def calculate_pressure(self):

        if self.pressure is not None:
            raise ValueError("pressure already exists")

        if (self.volume is None or self.mole is None or self.temperature is None):
            raise ValueError("volume, mole and temperature are required")

        return (self.mole._mol * gas_constant * self.temperature._kelvin) / self.volume._liter

    @property
    def calculate_volume(self):

        if self.volume is not None:
            raise ValueError("pressure already exists")

        if (self.pressure is None or self.mole is None or self.temperature is None):
            raise ValueError("volume, mole and temperature are required")

        return (self.mole._mol * gas_constant * self.temperature._kelvin) / self.pressure._atmosphere

    @property
    def calculate_mole(self):

        if self.mole is not None:
            raise ValueError("pressure already exists")

        if (self.pressure is None or self.volume is None or self.temperature is None):
            raise ValueError("volume, mole and temperature are required")

        return (self.pressure._atmosphere * self.volume._liter) / (gas_constant * self.temperature._kelvin)

    @property
    def calculate_temperature(self):

        if self.temperature is not None:
            raise ValueError("pressure already exists")

        if (self.pressure is None or self.volume is None or self.mole is None):
            raise ValueError("volume, mole and temperature are required")

        return (self.pressure._atmosphere * self.volume._liter) / (self.mole._mol * gas_constant)
