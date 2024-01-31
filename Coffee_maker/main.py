from data import MENU

# TODO :3a print the report of the machine, this will return the current levels of resource available in the machine

report = {"ingredients": {"water": 200,
                          "milk": 400,
                          "coffee": 200},
          "money": 2.5}


# TODO : 4a, 4b, 4c check if there is sufficient resources in the machine to serve the order
def coffee_machine(order):
    required_ingredients = MENU[order]["ingredients"]
    available_ingredients = report["ingredients"]
    available_money = report["money"]
    order_cost = MENU[order]["cost"]
    scarce_ingredients = []
    ingredients_used = []
    sale = 0

    for ingredient, amount in required_ingredients.items():
        if available_ingredients.get(ingredient, 0) < amount:
            scarce_ingredients.append(ingredient)
            if len(scarce_ingredients) != 0:
                print(f"Sorry, there is not enough 🫤 {', '.join(scarce_ingredients)} to make your order, We are poor 🫠")
                answer = input("Would you like us to restock? Type 'restock' ")
                if answer == 'restock':
                    report["ingredients"][ingredient] += amount
                else:
                    break

        elif available_ingredients.get(ingredient, 0) >= amount:

            # TODO:  5a, 5b, 5c prompt the user for money
            quarters = int(input("Please insert quarters 🪙: "))
            dimes = int(input("Please insert dimes 👛: "))
            nickles = int(input("Please insert nickles 💰: "))
            pennies = int(input("Please insert pennies 🤑: "))
            money_received = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

            if money_received < order_cost:
                print(
                    f'Sorry, that\'s not enough money 😞, your {order} costs ${order_cost}. \nYou are short by ${order_cost - money_received} \nYour money is refunded')
            # TODO: 6 a,b,c Check for successful transaction.
            else:
                sale = available_money + money_received
                change = round((money_received - order_cost), 3)
                print(f"Here you go your change, ${change} 💸")
                print(f"Enjoy your {order} ☕")
                break

    return sale

# TODO : 1a prompt the user and ask them what they like
# TODO : 1b The prompt should show everytime.

cafe_closed = False
while not cafe_closed:

    order = input("What would you like to drink? (espresso/latte/cappuccino) 🍵: ")
    # TODO : 2a Create a prompt to turn of the machine
    if order == "off":
        cafe_closed = True
    elif order == "report":
        print(f"Water 💧: {report['ingredients']['water']}ml\nMilk 🥛: {report['ingredients']['milk']}ml\nCoffee ☕: {report['ingredients']['coffee']}g\nMoney 💵: ${report['money']}")
    else:
        sale = coffee_machine(order)
        report["money"] += sale
        for ingredient, amount in MENU[order]["ingredients"].items():
            if ingredient in report["ingredients"]:
                report["ingredients"][ingredient] -= amount
    reorder = input("Would you like another drink?💁‍ Type 'y' for yes and 'n' for no: ")
    if reorder == 'y':
        continue
    else:
        print("Alrighty we are closing up now 🤗")
        cafe_closed = True



