from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

cafe_closed = False
while not cafe_closed:
    drink = input(f"What would you like to drink? {menu.get_items()} 🍵: ")
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
