import math as m
import time

answer = ''
message = """
 + for Addition 
 - for Substraction

 x for Multiplication
 / for Division

 pw for Raised to Power
 exit to exit
"""

thankyou = '''
© Srinikesh 2021-31 
This is The basic Calculator made with Python®

Thank you for using The-CalculatorApp
'''

print(f">{message}")


def add(user_input):
    user = user_input.split('+')
    num1 = int(user[0])
    num2 = int(user[1])
    print(f'>{num1+num2}')


def minus(user_input):
    user = user_input.split('-')
    num1 = int(user[0])
    num2 = int(user[1])
    print(f'>{num1-num2}')


def mult(user_input):
    user = user_input.split('x')
    num1 = int(user[0])
    num2 = int(user[1])
    print(f'>{num1*num2}')


def div(user_input):
    user = user_input.split('/')
    num1 = int(user[0])
    num2 = int(user[1])
    print(f'>{num1/num2}')


def sum_of(user_input):
    usr = user_input.split(' ')
    num = int(usr[1])
    while num > 0:
        sum = sum+(num % 10)
        num = num//10
    print(f'>{sum}')


def pw(user_input):
    try:
        if 'pw' in user_input:
            user = user_input.split('pw')
            num1 = int(user[0])
            num2 = int(user[1])
            print(f'>{m.pow(num1, num2)}')

        elif 'pW' in user_input:
            user = user_input.split('pW')
            num1 = int(user[0])
            num2 = int(user[1])
            print(f'>{m.pow(num1, num2)}')
        elif 'Pw' in user_input:
            user = user_input.split('Pw')
            num1 = int(user[0])
            num2 = int(user[1])
            print(f'>{m.pow(num1, num2)}')
        else:
            user = user_input.split('PW')
            num1 = int(user[0])
            num2 = int(user[1])
            print(f'>{m.pow(num1, num2)}')
    except ValueError:
        print(">Oops.. You can only use numbers for exponention !!")
    except OverflowError:
        print('>That was too big.. try it with a small number!!')


while True:
    user_input = input('> ')
    if user_input == 'help':
        print(message)
    elif 'exit' in user_input:
        print(thankyou)
        time.sleep(5)
        break
    elif 'sum of' or 'sumof' in user_input:
        sum_of(user_input)
    elif 'pw' or 'PW' or 'Pw' or 'pW' in user_input:
        pw(user_input)
    elif '/' in user_input:
        try:
            div(user_input)
        except ValueError:
            print(">Oops.. You can only use numbers for division !!")
        except ZeroDivisionError:
            print("You can't divide by zero")
    elif 'x' in user_input:
        try:
            mult(user_input)
        except ValueError:
            print(">Oops.. You can only use numbers for multiplication !!")

    elif '+' in user_input:
        try:
            add(user_input)
        except ValueError:
            print(">Oops.. You can only use numbers for addition !!")

    elif '-' in user_input:
        try:
            minus(user_input)
        except ValueError:
            print(">Oops.. You can only use numbers for subtraction !! ")

    else:
        print('Please type an expression')
