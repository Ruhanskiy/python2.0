__author__ = 'Molodtsov Ruslan'

'''
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''


def div(*args):

    try:
        arg1 = int(input("Input devident "))
        arg2 = int(input("Input devider "))
        res = arg1 / arg2
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null")
    '''


print(f'result {div()}')
