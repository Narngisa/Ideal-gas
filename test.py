import pyIdeal_gas

def main():
    gas = pyIdeal_gas.PVnRT(pressure=0, volume=5, mol=7, temperature=300)
    print(gas.calculate_pressure())

if __name__ == "__main__":
    main()
