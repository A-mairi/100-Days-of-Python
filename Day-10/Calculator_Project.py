import Calculator_Art


def add(n1, n2):
    """addition
    """
    return n1 + n2


def subtract(n1, n2):
    """subtraction
    """
    return n1 - n2


def multiply(n1, n2):
    """multiplication
    """
    return n1 * n2


def divide(n1, n2):
    """division
    """
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(Calculator_Art.logo)
    more_calculations = True
    first_number = float(input('What is the first number?: '))
    while more_calculations:
        for sign in operations:
            print(sign)
        user_operation = input('Which Operation would you like to use?: ')
        second_number = float(input('What is the second number?: '))
        result = operations[user_operation](first_number, second_number)
        print(f'{first_number} {user_operation} {second_number} = {result}')

        ask_user = input(f'Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ')

        if ask_user == 'y':
            first_number = result
        else:
            more_calculations = False
            print('\n' * 30)
            calculator()


calculator()
