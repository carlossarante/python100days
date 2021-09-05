import sys

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

money = {
    "money_earned": 0,
}

def command_turn_off():
    print('Turning off...')
    sys.exit(0)

def command_print_report():
    print('Water {}'.format(resources['water']))
    print('Milk {}'.format(resources['milk']))
    print('Coffee {}'.format(resources['coffee']))
    print('Money {}'.format(money['money_earned']))

def check_if_resources_are_sufficient(selected_coffee):
    for resource in resources:
        try:
            if MENU[selected_coffee]['ingredients'][resource] > resources[resource]:
                print('Sorry, there is not enough {}'.format(resource))
                return False
        except KeyError:
            continue

    return True

def check_coffee_name_is_valid(coffee_name):
    return coffee_name == 'espresso' or coffee_name == 'latte' or coffee_name == 'cappuccino'

def check_command(special__command):
    lowered_case_command = special__command.lower()

    if lowered_case_command == 'off':
        command_turn_off()
    elif lowered_case_command == 'print report':
        command_print_report()
    else:
        print('This coffee drink is not available')

def take_money():
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))

    return quarters * .25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.05


def make_coffee(selected_coffee):
    for resource in resources:
        try:
            resources[resource] = resources[resource] - MENU[selected_coffee]['ingredients'][resource]
        except KeyError:
            continue

def calculate_change(deposited_money, coffee_cost):
    return deposited_money - coffee_cost

def start_order(selected_coffee):
    if check_if_resources_are_sufficient(selected_coffee):
        deposited_money = take_money()
        coffee_cost = MENU[selected_coffee]['cost']

        if deposited_money >= coffee_cost:
            change = calculate_change(deposited_money, coffee_cost)
            money['money_earned'] += deposited_money - change
            make_coffee(selected_coffee)

            print('Here is your {}, Enjoy!'.format(selected_coffee))

            if change > 0:
                print('Here is {:.2f} dollars in change'.format(change))
        else:
            print('Sorry that\'s not enough money. Money refunded.')




def take_order():
    ordered_coffee = input('What would you like? (espresso|late|cappuccino) ')

    if check_coffee_name_is_valid(ordered_coffee):
        start_order(ordered_coffee)
    else:
        check_command(ordered_coffee)

    take_order()

if __name__ == '__main__':
    take_order()