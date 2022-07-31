from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
mu = Menu()
cfmk = CoffeeMaker()
m_mahchine = MoneyMachine()
while is_on:
    choice = input(f'what would you like? ({mu.get_items()}): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        cfmk.report()
        m_mahchine.report()
    else:
        drink = mu.find_drink(choice)
        if cfmk.is_resource_sufficient(drink):
            if m_mahchine.make_payment(drink.cost):
                cfmk.make_coffee(drink)


