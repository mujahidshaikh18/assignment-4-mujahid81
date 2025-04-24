import math

def pythagorean_theorem():
    # Get th two sides lengths from the user and cast them to be numbers
    ab: float = float(input("\033[1;3mEnter the length of side AB: \033[0m"))
    ac: float = float(input("\033[1;3mEnter the length of side AC: \033[0m"))

    # Calculate the hypotenuse using the two sides
    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of side BC (hypotenuse) is: " + str(bc))

if __name__ == "__main__":
    pythagorean_theorem()