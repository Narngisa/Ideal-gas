from ideal_gas import Pressure, Volume, Mole, Temperature, Gram, MolarMass, Density, Molarity
import pytest

def test_pressure_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported pressure unit"):
        p = Pressure(pressure=1, unit="atm")
        object.__setattr__(p, 'unit', "invalid")
        _ = p.atmosphere

def test_volume_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported volume unit"):
        v = Volume(volume=1, unit="L")
        object.__setattr__(v, 'unit', "invalid")
        _ = v.liter

def test_mole_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported mole unit"):
        m = Mole(mole=1, unit="mol")
        object.__setattr__(m, 'unit', "invalid")
        _ = m.mol

def test_temperature_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported temperature unit"):
        t = Temperature(temperature=0, unit="C")
        object.__setattr__(t, 'unit', "invalid")
        _ = t.kelvin

def test_gram_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported gram unit"):
        g = Gram(gram=1, unit="g")
        object.__setattr__(g, 'unit', "invalid")
        _ = g.grams

def test_molar_mass_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported molar mass unit"):
        mm = MolarMass(molar_mass=1, unit="g/mol")
        object.__setattr__(mm, 'unit', "invalid")
        _ = mm.gram_per_mol

def test_density_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported density unit"):
        d = Density(density=1, unit="g/L")
        object.__setattr__(d, 'unit', "invalid")
        _ = d.gram_per_liter

def test_molarity_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported molarity unit"):
        m = Molarity(molarity=1, unit="mol/L")
        object.__setattr__(m, 'unit', "invalid")
        _ = m.mol_per_liter
