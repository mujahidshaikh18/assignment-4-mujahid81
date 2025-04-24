def main():
    fahrenheit = float(input("\033[1;33mEnter temperature in Fahrenheit: \033[0m"))
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature : {fahrenheit}F = {celsius:.2f}C")

if __name__ == "__main__":
    main()
# The code converts a temperature from Fahrenheit to Celsius.