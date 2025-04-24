"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""
import random

NUM_SIDES = 6

def roll_dice():

    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Die1: {die1}, Die2: {die2}, Total of the two dice is: {total}")

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    for i in range(3):
        roll_dice()
        print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()  