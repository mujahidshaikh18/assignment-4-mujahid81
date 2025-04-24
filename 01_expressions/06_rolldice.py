"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
import random

NUM_SIDES = 6

def main():
    """
    Simulate rolling two dice, and prints results of each
    roll as well as the total.
    """
    # Simulate rolling two dice
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    # Calculate the total of the two dice
    total = die1 + die2

    # Display the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == "__main__":
    main()