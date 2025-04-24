def fruits_shop():
    fruits = {
        "apple": 2.5,
        "banana": 1.5,
        "orange": 3.0,
        "grape": 4.0,
        "kiwi": 5.0,
        "mango": 5.5,
        "pineapple": 6.0,
    }

    print("\t\t\033[1;35m***Welcome to the fruit shop!***\033[0m")
    print("Available fruits and their prices:")
    for fruit, price in fruits.items():
        print(f"{fruit.capitalize()}: ${price:.2f}")

    total_cost = 0
    while True:
        fruit = input("\033[1;3mEnter the fruit you want to buy: \033[0m")
        if fruit == "":
            break
        elif fruit in fruits:
            quantity = int(input(f"\033[1;3mHow many {fruit}s do you want? \033[0m"))
            total_cost += fruits[fruit] * quantity
            print(f"Added {quantity} {fruit}(s) to your cart.")
        else:
            print("Sorry, we don't have that fruit.")

    print("Your total cost is: $" + str(total_cost))
    print("\033[4;34mThank you for shopping with us!\033[0m")

if __name__ == "__main__":
    fruits_shop()
