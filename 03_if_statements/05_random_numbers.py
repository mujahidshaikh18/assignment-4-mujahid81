import random
# Generate a random number between 1 to 10

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for i in range(N_NUMBERS):
        num: list[int] = random.randint(MIN_VALUE, MAX_VALUE)
        print(num)

if __name__ == "__main__":
    main()