from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys


def process_input(coffee_maker, command):
    parsed_command = command.lower()

    if parsed_command == 'off':
        print('Turning off...')
        sys.exit(0)

    elif parsed_command == 'print report':
        coffee_maker.report()
        return None

    else:
        return menu.find_drink(parsed_command)


def start_order(current_menu, current_coffee_maker, current_money_machine):
    user_input = take_order(current_menu)

    found_drink = process_input(current_coffee_maker, user_input)

    if found_drink and current_coffee_maker.is_resource_sufficient(found_drink):
        money_received = current_money_machine.make_payment(found_drink.cost)

        if money_received:
            current_coffee_maker.make_coffee(found_drink)

    start_order(current_menu, current_coffee_maker, current_money_machine)


def take_order(current_menu):
    user_selection = input(f'What would you like? ({current_menu.get_items()}): ')

    return user_selection


if __name__ == '__main__':
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    start_order(menu, coffee_maker, money_machine)


