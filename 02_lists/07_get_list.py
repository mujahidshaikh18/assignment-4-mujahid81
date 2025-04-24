def main():
    lst = []

    val = input("\033[1;34mEnter a value: \033[0m") # Get an initial value
    while val: # Continue until the user enters an empty string
        lst.append(val) # Add the value to the list
        val = input("\033[1;34mEnter a value: \033[0m") # Get the next value

    print("Here the list:", lst) # Print the list

if __name__ == "__main__":
    main()