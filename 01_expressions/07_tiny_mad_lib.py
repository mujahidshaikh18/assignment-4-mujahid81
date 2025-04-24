SENTENCE_START: str = "Code in Place is fun. I learned to program and used Python to make my "

def main():
    adjective = input("\033[1;3mPlease type an adjective and press enter: \033[0m")
    noun = input("\033[1;3mPlease type a noun and press enter: \033[0m")
    verb = input("\033[1;3mPlease type a verb and press enter: \033[0m")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

if __name__ == "__main__":
    main()