cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_black_jack = False
user_black_jack = False
import random
computer_cards = random.sample(cards,2)
user_cards = random.sample(cards,2)
print(computer_cards)
print(user_cards)
if 11 in computer_cards and 10 in computer_cards:
    print("Computer has a black Jack")
    computer_black_jack = True
if 11 in user_cards and 10 in user_cards:
    print("User has a black Jack")
    user_black_jack = True
if computer_black_jack and user_black_jack:
    print("Computer Wins")
elif user_black_jack:
    print("User Wins")

def calculate_score(hand):
    total = sum(hand)
    if 11 in hand and total > 21:
        total = total - 10
    return total
print(f"The first Computer card:{computer_cards[0]}")

game_over = False
while not game_over:
    user_score = calculate_score(user_cards)
    print(f"Your cards: {user_cards} + Your score: {user_score}")
    if user_score > 21:
        print("Game over, Computer Wins, You went over 20")
        game_over = True
        break

    ask = input("User, do you want to get another card? y/n: ")
    if ask == "y":
        user_cards.append(random.choice(cards))
    else:
        game_over = True
if calculate_score(user_cards) <=21:
    while calculate_score(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nFinal User hand: {user_cards}, score: {user_score}")
    print(f"Final Computer hand: {computer_cards}, score: {computer_score}")
    if computer_score > 21:
        print("Computer went over 21. You win")
    elif computer_score > user_score:
        print("Computer Wins")
    elif computer_score < user_score:
        print("You win")
    else:
        print("Draw")





