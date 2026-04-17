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
# ---------------------------------------------

# TODO 1: Prompt user by asking "What would you like?"
is_on = True
profit = 0

def sufficient_resource(order_ingredients):
    '''Returns True when enough ingredients and False when not enough'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    '''Returns total calculated from coins inserted'''
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def check_transaction(money_received, drink_cost):
    '''Returns True if payment is sufficient and False when not'''
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_order, order_ingredients):
    '''Deduct ingredients from resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_order} \u2615. Enjoy!")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if sufficient_resource(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
