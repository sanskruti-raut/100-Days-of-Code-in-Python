MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
insufficient = True
while insufficient:

    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if ask == "report":
        print(f"Water:{resources['water']} ml")
        print(f"Milk:{resources['milk']} ml")
        print(f"Coffee:{resources['coffee']} g")
        #print(f"Money: $0")
    elif ask == "espresso" or ask == "latte" or ask == "cappuccino":
        drink = MENU[ask]
        can_make = True 
        for item in drink["ingredients"]:
            if drink["ingredients"][item] > resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        if can_make:
            print("Please insert coins")
            quarters = int(input("How many quarters?:")) * 0.25
            dimes = int(input("How many dimes?:")) * 0.10
            nickels = int(input("How many nickels?:")) * 0.05
            pennies = int(input("How many pennies?:")) * 0.01
            total = quarters + dimes + nickels + pennies
            if total < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(total - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {ask} ☕️. Enjoy!")
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
        else:
            print("Cannot make the drink due to insufficient resources.")
            insufficient = False
    else:
        print("Invalid input.")



