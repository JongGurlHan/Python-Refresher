number = 7
user_input = input("Enter 'y' if you would like to paly: ").lower()

if user_input == "y":
    user_number = int(input("guess your number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong!")