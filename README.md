# 💨Ideal Gas Module
Calculating The Ideal Gas Law in python, focusing make it easy and high school-friendly

> [!NOTE]
> This project under active development 🔥

## 🐍Language
Pure Python `version >= 3.10`

## ☕Features

### Unit
- Pressure `atm`, `Torr` and `mmHg`
- Volume `ml`, `cm3`, `L` and `dm3`
- Mole `mol`
- Temperature `C` and `K`
- Gram `g` and `kg`
- Molar mass `g/mol`

### Config Value
- Gas Constant (R) `0.0821`
- Kelvin (K) `273`

### Function
- PV=nRT
- PV=(g/M)RT

## ⚙️Install
You can download file ideal_gas.py and import it to use in your file main.

## 📃Example

### PV = nRT
```py
from ideal_gas import PVnRT, Volume, Mole, Temperature
# Pressure, Volume, Mole, Temperature

gas = PVnRT(
    volume=Volume(volume=7600, unit="ml"),
    mole=Mole(mole=8, unit="mol"),
    temperature=Temperature(temperature=27, unit="C"),
)

# Pressure ~ 25.92631
print(gas.calculate_pressure)
```

### PV = (g/M)RT
```py
from ideal_gas import PVgMRT, Volume, Gram, MolarMass, Temperature
# Pressure, Volume, Gram, MolarMass, Temperature

gas = PVgMRT(
    volume=Volume(volume=400, unit="ml"),
    gram=Gram(gram=5, unit="kg"),
    molar_mass=MolarMass(molar_mass=4, unit="g/mol"),
    temperature=Temperature(temperature=298, unit="K"),
)

# Pressure ~ 76,455.625
print(gas.calculate_pressure)
```

## 🔧Test Module
1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install pytest`
4. `pip install -e .`
5. `pytest`
