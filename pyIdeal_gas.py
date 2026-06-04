from dataclasses import dataclass, KW_ONLY

@dataclass
class Unit:
    _: KW_ONLY
    pressure: float
    volume: float
    temperature: float
    unit: str

    @property
    def atmosphere(self):
        if self.unit == "Torr" or self.unit == "mmHg":
            return self.pressure / 760

        elif self.unit == "Pa":
            return self.pressure / 101326

        else:
            raise ValueError("All values are already set - Torr, mmHg and Pa")

    @property
    def liters(self):
        if self.unit == "mL" or self.unit == "cm3":
            return self.volume / 1000
        else:
            raise ValueError("All values are already set - mL or cm3\n Info: dm3 = L")



@dataclass
class Factor:
    _: KW_ONLY
    pressure: Unit | None = None
    volume: Unit | None = None
    mol: float | None = None
    gas_constant: float = 0.0821
    temperature: Unit | None = None

    @property
    def PVnRT(self):
        if self.pressure is None:
            if self.volume is None or self.mol is None or self.temperature is None:
                raise ValueError("volume, mol, and temperature must be set to solve for pressure.")
            self.pressure = (self.mol * self.gas_constant * self.temperature) / self.volume.liters
            return self.pressure

        elif self.volume is None:
            if self.pressure is None or self.mol is None or self.temperature is None:
                raise ValueError("pressure, mol and temperature must be set to solve for volume.")
            self.volume = (self.mol * self.gas_constant * self.temperature) / self.pressure.atmosphere
            return self.volume

        elif self.mol is None:
            if self.pressure is None or self.volume is None or self.temperature is None:
                raise ValueError("pressure, volume and temperature must be set to solve for mol.")
            self.mol = (self.pressure.atmosphere * self.volume.liters) / (self.gas_constant * self.temperature)
            return self.mol

        elif self.temperature is None:
            if self.pressure is None or self.volume is None or self.mol is None:
                raise ValueError("pressure, volume and mol must be set to solve for temperature.")
            self.temperature = (self.pressure * self.volume) / (self.mol * self.gas_constant)
            return self.temperature

        else:
            raise ValueError("All values are already set — nothing to solve! !!")
