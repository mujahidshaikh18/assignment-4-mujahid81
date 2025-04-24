c: int = 299792458 # speed of light in m/s

def main():
    mass_in_kg: float = float(input("\033[1;3mEnter the mass in kg: \033[0m"))
    # Calculate energy using E=mc^2
    # equivalent energy = mass * (c ** 2)
    # using the ** operator to raise c to the power of 2
    energy_in_joules: float = mass_in_kg * (c ** 2)

    # Display work to the user
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(c) + " m/s")

    print(str(energy_in_joules) + " Joules of energy!")

if __name__ == "__main__":
    main()