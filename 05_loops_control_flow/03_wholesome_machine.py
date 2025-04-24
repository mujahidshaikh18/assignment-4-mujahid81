AFFIRMATION : str = "I am a capable of doing anything I put my mind to."

def main():
    print("\033[1;34mPlease type a following affirmation: \033[0m" + AFFIRMATION)

    user_feedback: str = input()
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")

        print("\033[1;34mPlease type a following affirmation: \033[0m" + AFFIRMATION)
        user_feedback = input()

    print("That's rigth! :)")
 

if __name__ == "__main__":
    main()