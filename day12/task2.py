import random
attempts = 0

print(" Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100 ")

ask = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if ask == "easy":
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
else:
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5

actual_num = random.randint(1,100)
guess = int(input("Make a guess: "))

while attempts:

    if guess > actual_num:
        print("Too High")
        print("Guess Again")
        attempts -= 1

    elif guess < actual_num:
        print("Too Low")
        print("Guess Again")
        attempts -= 1
    else:
        print(f"You got it! the answer was {actual_num}")
        break

    if attempts > 0:
        print(f"You have {attempts} attempts remaining. Guess again.")
        guess = int(input("Make a guess: "))
    else:
        print("You've run out of attempts. You lose!")
        print(f"The answer was {actual_num}")




