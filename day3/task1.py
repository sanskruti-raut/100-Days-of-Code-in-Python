print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == 'S':
    cost = 15
elif size == 'M':
    cost = 20
elif size == 'L':
    cost = 25

# Pepperoni price
if pepperoni == 'Y':
    if size == 'S':
        cost += 2
    else:
        cost += 3

# Cheese price
if extra_cheese == 'Y':
    cost += 1

print(f"Your final bill is: ${cost}")
