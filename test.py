import pyIdeal_gas

def main():
    gas = pyIdeal_gas.PVnRT(volume=5, mol=7, temperature=300)
    print(gas._PVnRT)

if __name__ == "__main__":
    main()
