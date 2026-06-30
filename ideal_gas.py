from dataclasses import dataclass, field
from typing import Optional, Literal

PressureUnit = Literal["atm", "Torr", "mmHg"]
VolumeUnit = Literal["ml", "cm3", "L", "dm3"]
MoleUnit = Literal["mol"]
TemperatureUnit = Literal["K", "C"]
GramUnit = Literal["g", "kg"]
MolarMassUnit = Literal["g/mol"]
DensityUnit = Literal["g/L", "g/dm3"]
MolarityUnit = Literal["mol/dm3", "mol/L"]

# Gas Constant Value
GAS_CONSTANT_DEFAULT = 0.082057
GAS_CONSTANT_SCHOOL = 0.0821

@dataclass(kw_only=True)
class Pressure:
    pressure: float
    unit: PressureUnit

    def __post_init__(self):
        if self.pressure <= 0:
            raise ValueError("Pressure must be greater than zero")


    @property
    def atmosphere(self) -> float:
        if self.unit == "atm":
            return self.pressure
        elif self.unit == "Torr" or self.unit == "mmHg":
            return self.pressure / 760
        raise ValueError(f"Unsupported pressure unit: {self.unit}")

@dataclass(kw_only=True)
class Volume:
    volume: float
    unit: VolumeUnit

    def __post_init__(self):
        if self.volume <= 0:
            raise ValueError("Volume must be greater than zero")

    @property
    def liter(self) -> float:
        if self.unit == "L" or self.unit == "dm3":
            return self.volume
        elif self.unit == "ml" or self.unit == "cm3":
            return self.volume / 1000
        raise ValueError(f"Unsupported volume unit: {self.unit}")

@dataclass(kw_only=True)
class Mole:
    mole: float
    unit: MoleUnit

    def __post_init__(self):
        if self.mole <= 0:
            raise ValueError("Mole must be greater than zero")

    @property
    def mol(self) -> float:
        if self.unit == "mol":
            return self.mole
        raise ValueError(f"Unsupported mole unit: {self.unit}")

@dataclass(kw_only=True)
class GasConstant:
    school_mode: bool = False

    @property
    def gas_mode(self) -> float:
        return GAS_CONSTANT_SCHOOL if self.school_mode else GAS_CONSTANT_DEFAULT

@dataclass(kw_only=True)
class Temperature:
    temperature: float
    unit: TemperatureUnit

    def __post_init__(self):
        if self.kelvin <= 0:
            raise ValueError("Temperature must be greater than zero")

    @property
    def kelvin(self) -> float:
        if self.unit == "K":
            return self.temperature
        elif self.unit == "C":
            return self.temperature + 273
        raise ValueError(f"Unsupported temperature unit: {self.unit}")

@dataclass(kw_only=True)
class Gram:
    gram: float
    unit: GramUnit

    def __post_init__(self):
        if self.gram <= 0:
            raise ValueError("Gram must be greater than zero")

    @property
    def grams(self) -> float:
        if self.unit == "g":
            return self.gram
        elif self.unit == "kg":
            return self.gram * 1000
        raise ValueError(f"Unsupported gram unit: {self.unit}")

@dataclass(kw_only=True)
class MolarMass:
    molar_mass: float
    unit: MolarMassUnit

    def __post_init__(self):
        if self.molar_mass <= 0:
            raise ValueError("Molar mass must be greater than zero")

    @property
    def gram_per_mol(self) -> float:
        if self.unit == "g/mol":
            return self.molar_mass
        raise ValueError(f"Unsupported molar mass unit: {self.unit}")

@dataclass(kw_only=True)
class Density:
    density: float
    unit: DensityUnit

    def __post_init__(self):
        if self.density <= 0:
            raise ValueError("Density must be greater than zero")

    @property
    def gram_per_liter(self) -> float:
        if self.unit == "g/L" or self.unit == "g/dm3":
            return self.density
        raise ValueError(f"Unsupported density unit: {self.unit}")

@dataclass(kw_only=True)
class Molarity:
    molarity: float
    unit: MolarityUnit

    def __post_init__(self):
        if self.molarity <= 0:
            raise ValueError("Molarity must be greater than zero")

    @property
    def mol_per_liter(self) -> float:
        if self.unit == "mol/L" or self.unit == "mol/dm3":
            return self.molarity
        raise ValueError(f"Unsupported density unit: {self.unit}")

@dataclass(kw_only=True)
class PVnRT:
    pressure: Optional[Pressure] = None
    volume: Optional[Volume] = None
    mole: Optional[Mole] = None
    temperature: Optional[Temperature] = None
    gas_constant: GasConstant = field(default_factory=lambda: GasConstant())

    @property
    def calculate_pressure(self):

        if self.pressure is not None:
            raise ValueError("pressure already exists")

        if (self.volume is None or self.mole is None or self.temperature is None):
            raise ValueError("volume, mole, and temperature are required")

        return (self.mole.mol * self.gas_constant.gas_mode * self.temperature.kelvin) / self.volume.liter

    @property
    def calculate_volume(self):

        if self.volume is not None:
            raise ValueError("volume already exists")

        if (self.pressure is None or self.mole is None or self.temperature is None):
            raise ValueError("pressure, mole, and temperature are required")

        return (self.mole.mol * self.gas_constant.gas_mode * self.temperature.kelvin) / self.pressure.atmosphere

    @property
    def calculate_mole(self):

        if self.mole is not None:
            raise ValueError("mole already exists")

        if (self.pressure is None or self.volume is None or self.temperature is None):
            raise ValueError("pressure, volume, and temperature are required")

        return (self.pressure.atmosphere * self.volume.liter) / (self.gas_constant.gas_mode * self.temperature.kelvin)

    @property
    def calculate_temperature(self):

        """Return temperature in Kelvin"""

        if self.temperature is not None:
            raise ValueError("temperature already exists")

        if (self.pressure is None or self.volume is None or self.mole is None):
            raise ValueError("pressure, volume, and mole are required")

        return (self.pressure.atmosphere * self.volume.liter) / (self.mole.mol * self.gas_constant.gas_mode)

@dataclass(kw_only=True)
class PVgMRT:
    pressure: Optional[Pressure] = None
    volume: Optional[Volume] = None
    gram: Optional[Gram] = None
    molar_mass: Optional[MolarMass] = None
    temperature: Optional[Temperature] = None
    gas_constant: GasConstant = field(default_factory=lambda: GasConstant())

    @property
    def calculate_pressure(self):
        if self.pressure is not None:
            raise ValueError("pressure already exists")

        if (self.volume is None or self.gram is None or self.molar_mass is None or self.temperature is None):
            raise ValueError("volume, gram, molar mass, and temperature are required")

        return ((self.gram.grams / self.molar_mass.gram_per_mol) * self.gas_constant.gas_mode * self.temperature.kelvin) / self.volume.liter

    @property
    def calculate_volume(self):
        if self.volume is not None:
            raise ValueError("volume already exists")
        if (self.pressure is None or self.gram is None or self.molar_mass is None or self.temperature is None):
            raise ValueError("pressure, gram, molar mass, and temperature are required")

        return ((self.gram.grams / self.molar_mass.gram_per_mol) * self.gas_constant.gas_mode * self.temperature.kelvin) / self.pressure.atmosphere

    @property
    def calculate_gram(self):
        if self.gram is not None:
            raise ValueError("gram already exists")
        if (self.pressure is None or self.volume is None or self.molar_mass is None or self.temperature is None):
            raise ValueError("pressure, volume, molar mass, and temperature are required")

        return (self.pressure.atmosphere * self.volume.liter * self.molar_mass.gram_per_mol) / (self.gas_constant.gas_mode * self.temperature.kelvin)

    @property
    def calculate_molar_mass(self):
        if self.molar_mass is not None:
            raise ValueError("molar mass already exists")
        if (self.pressure is None or self.volume is None or self.gram is None or self.temperature is None):
            raise ValueError("pressure, volume, gram, and temperature are required")

        return (self.gram.grams * self.gas_constant.gas_mode * self.temperature.kelvin) / (self.pressure.atmosphere * self.volume.liter)

    @property
    def calculate_temperature(self):
        if self.temperature is not None:
            raise ValueError("temperature already exists")
        if (self.pressure is None or self.volume is None or self.gram is None or self.molar_mass is None):
            raise ValueError("pressure, volume, gram, and molar mass are required")

        return (self.pressure.atmosphere * self.volume.liter * self.molar_mass.gram_per_mol) / (self.gram.grams * self.gas_constant.gas_mode)

@dataclass(kw_only=True)
class PVdRT:
    pressure: Optional[Pressure] = None
    volume: Optional[Volume] = None
    density: Optional[Density] = None
    temperature: Optional[Temperature] = None
    gas_constant: GasConstant = field(default_factory=lambda: GasConstant())

    @property
    def calculate_pressure(self):
        if self.pressure is not None:
            raise ValueError("pressure already exists")
        if (self.volume is None or self.density is None or self.temperature is None):
            raise ValueError("volume, density, and temperature are required")

        return (self.density.gram_per_liter * self.gas_constant.gas_mode * self.temperature.kelvin) / self.volume.liter

    @property
    def calculate_volume(self):
        if self.volume is not None:
            raise ValueError("volume already exists")
        if (self.pressure is None or self.density is None or self.temperature is None):
            raise ValueError("pressure, density, and temperature are required")

        return (self.density.gram_per_liter * self.gas_constant.gas_mode * self.temperature.kelvin) / self.pressure.atmosphere

    @property
    def calculate_density(self):
        if self.density is not None:
            raise ValueError("density already exists")
        if (self.pressure is None or self.volume is None or self.temperature is None):
            raise ValueError("pressure, volume, and temperature are required")

        return (self.pressure.atmosphere * self.volume.liter) / (self.gas_constant.gas_mode * self.temperature.kelvin)

    @property
    def calculate_temperature(self):
        if self.temperature is not None:
            raise ValueError("temperature already exists")
        if (self.pressure is None or self.volume is None or self.density is None):
            raise ValueError("pressure, volume, and density are required")

        return (self.pressure.atmosphere * self.volume.liter) / (self.density.gram_per_liter * self.gas_constant.gas_mode)

@dataclass(kw_only=True)
class PMRT:
    pressure: Optional[Pressure] = None
    molarity: Optional[Molarity] = None
    temperature: Optional[Temperature] = None
    gas_constant: GasConstant = field(default_factory=lambda: GasConstant())

    @property
    def calculate_pressure(self):
        if self.pressure is not None:
            raise ValueError("pressure already exists")
        if (self.molarity is None or self.temperature is None):
            raise ValueError("molarity, and temperature are required")

        return (self.molarity.mol_per_liter * self.gas_constant.gas_mode * self.temperature.kelvin)

    @property
    def calculate_molarity(self):
        if self.molarity is not None:
            raise ValueError("molarity already exists")
        if (self.pressure is None or self.temperature is None):
            raise ValueError("pressure, and temperature are required")

        return (self.pressure.atmosphere / (self.gas_constant.gas_mode * self.temperature.kelvin))

    @property
    def calculate_temperature(self):
        if self.temperature is not None:
            raise ValueError("temperature already exists")
        if (self.pressure is None or self.molarity is None):
            raise ValueError("pressure, and molarity are required")

        return (self.pressure.atmosphere / (self.molarity.mol_per_liter * self.gas_constant.gas_mode))
