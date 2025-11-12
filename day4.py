print("We are building Rock Paper Scissors game?" )
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
import random
computer_choice = random.randint(0,2)
if user_input == "0":
    print("You chose: Rock")
    if computer_choice == 0:
        print("Computer chose: Rock")
        print("It's a draw")
    elif computer_choice == 1:
        print("Computer chose: Paper")
        print("You lose")
    else:
        print("Computer chose: Scissors")
        print("You win")
elif user_input == "1":
    print("You chose: Paper")
    if computer_choice == 0:
        print("Computer chose: Rock")
        print("You win")
    elif computer_choice == 1:
        print("Computer chose: Paper")
        print("It's a draw")
    else:
        print("Computer chose: Scissors")
        print("You lose")
elif user_input == "2":
    print("You chose: Scissors")
    if computer_choice == 0:
        print("Computer chose: Rock")
        print("You lose")
    elif computer_choice == 1:
        print("Computer chose: Paper")
        print("You win")
    else:
        print("Computer chose: Scissors")
        print("It's a draw")
else:
    print("Invalid input! You must type 0, 1, or 2.")


