INCHES_IN_FOOT: int = 12

def feet_to_inches():
    feet = float(input("Enter the number of feet: "))
    inches = feet * INCHES_IN_FOOT
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == "__main__":
    feet_to_inches()