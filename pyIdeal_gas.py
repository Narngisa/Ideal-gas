class PVnRT:
    def __init__(self, pressure: float, volume: float, mol: float, temperature: float):
        self.pressure = pressure
        self.volume = volume
        self.mol = mol
        self.gas_constant = 0.0821
        self.temperature = temperature

    def calculate_pressure(self):
        return (self.mol * self.gas_constant * self.temperature) / self.volume

    def calculate_volume(self):
        return (self.mol * self.gas_constant * self.temperature) / self.pressure

    def calculate_mol(self):
        return (self.pressure * self.volume) / (self.gas_constant * self.temperature)

    def calculate_temperature(self):
        return (self.pressure * self.volume) / (self.mol * self.gas_constant)
