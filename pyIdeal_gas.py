from dataclasses import dataclass, KW_ONLY

@dataclass
class PVnRT:
    _: KW_ONLY
    pressure: float | None = None
    volume: float | None = None
    mol: float | None = None
    gas_constant: float = 0.0821
    temperature: float | None = None

    @property
    def _PVnRT(self):
        if self.pressure is None:
            if self.volume is None or self.mol is None or self.temperature is None:
                raise ValueError("volume, mol, and temperature must be set to solve for pressure.")
            self.pressure = (self.mol * self.gas_constant * self.temperature) / self.volume
            return self.pressure

        elif self.volume is None:
            if self.pressure is None or self.mol is None or self.temperature is None:
                raise ValueError("pressure, mol and temperature must be set to solve for volume.")
            self.volume = (self.mol * self.gas_constant * self.temperature) / self.pressure
            return self.volume

        elif self.mol is None:
            if self.pressure is None or self.volume is None or self.temperature is None:
                raise ValueError("pressure, volume and temperature must be set to solve for mol.")
            self.mol = (self.pressure * self.volume) / (self.gas_constant * self.temperature)
            return self.mol

        elif self.temperature is None:
            if self.pressure is None or self.volume is None or self.mol is None:
                raise ValueError("pressure, volume and mol must be set to solve for temperature.")
            self.temperature = (self.pressure * self.volume) / (self.mol * self.gas_constant)
            return self.temperature

        else:
            raise ValueError("All values are already set — nothing to solve! !!")
