MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18},
        "cost": 1.5},

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24, },
        "cost": 2.5},

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24, },
        "cost": 3.0
    }
}


resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# TODO: 1. Prompt user asking 'What would you like (espresso/latte/cappuccino)
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
# TODO: 3. Check resources sufficient when user chooses a drink
# TODO: 4. Process coins inserted
# TODO: 5. Check if transaction successful
# TODO: 6. Make coffee using recipes
# TODO: 7. Print report of the current resource values by entering "report"


def get_report():
    return f'Water: {resource["water"]}ml\nMilk: {resource["milk"]}ml\nCoffee: {resource["coffee"]}g\nMoney: ${resource["money"]}'


def check_resources(coffee):
    for i in ("water", "milk", "coffee"):
        return True if (resource[i] - MENU[coffee]['ingredients'][i]) >= 0 else print(f"Sorry there is not enough {i}.")


def update_resources(coffee):
    for i in ("water", "milk", "coffee"):
        resource[i] -= MENU[coffee]['ingredients'][i]

def process_coins():
    print("Please insert coins.")
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickles = 0.05 * int(input("How many nickles?: "))
    pennies = 0.01 * int(input("How many pennies?: "))
    return quarters + dimes + nickles + pennies


def make_coffee():
    while True:
        response = input(
            'What would you like? (espresso/latte/cappuccino): ').lower().strip()

        if response in ["espresso", "latte", "cappuccino"]:
            if check_resources(response):
                payment = process_coins()
                if payment >= (cost := MENU[response]["cost"]):
                    resource["money"] += MENU[response]["cost"]
                    update_resources(response)
                    print(f'Here is ${round(payment - cost, 2)} in change')
                    print(f'Here is your {response} ☕ Enjoy!')
                else:
                    print("Sorry that's not enough money. Money refunded.")
        elif response == "report":
            print(get_report())
        elif response == "off":
            break


print(make_coffee())
