MINIMUM_HEIGHT : int = 50

def main():
    # Get the user's height in inches
    height : int = int(input("\033[1;3mHow tall are you?: \033[0m"))

    # Check if the user is tall enough to ride
    if height >= MINIMUM_HEIGHT:
        print("You are tall enough to ride!")
    else:
        print("You are not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()