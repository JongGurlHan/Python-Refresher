number = 7

while True:

    user_input = input("Would you like to play? (Y/n) ") #n이 아닌 모든 입력값에 Y로 인식한다 (convention)

    if user_input == "n":
        break

    user_number = int(input("guess your number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong!")    