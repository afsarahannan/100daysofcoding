from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#initiate the object with the menu class
# menu = Menu()
# drink = "espresso"

#use the find_drink method to return where the drink is stored.
# order = menu.find_drink(drink)

#use the attributes of the menuitem class to call the name, cost and the ingredients of the object
# print(order.name)
# print(order.cost)
# print(order.ingredients)

#initiate the coffee object with the coffee making class
# coffee = CoffeeMaker()
# coffee.report()

#using the attribute from the coffemaker class to check if there is enough resource
#will return true if there is enough resource
# print(coffee.is_resource_sufficient(order))

#return the enjoy your coffee statement and deducts the amount from the resources dictionary
# coffee.make_coffee(order)

#initiate the money object with the money machine class
# money = MoneyMachine()

#returns the report of how much profit was made
# money.report()

#returns the total coins processed from the payment
# print(money.process_coins())

#calls the payment option of asking to insert coins for the particular drink ordered
#the make payment method is inside the make_payment function and it returns the change
# money.make_payment(order.cost)

################################################## Coffee-maker oop ##########################################################

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

cafe_closed = False
while not cafe_closed:
    options = menu.get_items()
    drink = input(f"What would you like to drink? {options} 🍵: ")
    if drink == "report":
        coffee.report()
        money.report()
    elif drink == "off":
        cafe_closed = True

    else:
        order = menu.find_drink(drink)
        if coffee.is_resource_sufficient(order):
            if money.make_payment(order.cost):
                coffee.make_coffee(order)
                reorder = input("Would you like another drink?💁‍ Type 'y' for yes and 'n' for no: ")
                if reorder == 'y':
                    print("Let me get the menu for you")
                else:
                    print("Alrighty we are closing up now 🤗")
                    cafe_closed = True
            else:
                print(f"The cost of {order.name} is ${order.cost} and you gave ${money.money_received}")



