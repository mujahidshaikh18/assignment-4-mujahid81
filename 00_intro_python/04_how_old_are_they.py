def main():
    anton: int = 21 # Anton's age is given as 21 years old
    beth: int = 6 + anton # Beth's age is 6 years older than Anton, so add 6 to Anton's age to get Beth's age
    chen: int = 20 + beth# Chen's age is 20 years older than Beth, so add 20 to Beth's age to get Chen's age
    drew: int = chen + anton #Drew is as old as chen's age plus anton's age, so them together
    ethan: int = chen # Ethan is the same age as chen, so set Ethan's age equal to Chen's age
    
    # Print the ages of all the characters
    print("Anton's age is" + str(anton))
    print("Beth's age is" + str(beth))
    print("Chen's age is" + str(chen))
    print("Drew's age is" + str(drew))
    print("Ethan's age is" + str(ethan))

if __name__ == "__main__":
    main()