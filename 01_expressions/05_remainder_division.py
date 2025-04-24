def main():
    # This program demonstrates the use of the modulus operator to find the remainder of a division operation.
    dividend: int = int(input("\033[1;3mPlease enter an integer to be divided: \033[0m"))
    divisor: int = int(input("\033[1;3mPlease enter an integer to be divide by: \033[0m"))

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    print("The result of this division is "+ str(quotient) + " with a remainder of " + str(remainder))

if __name__ == "__main__":
    main()