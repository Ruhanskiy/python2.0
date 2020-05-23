__author__ = 'Molodtsov Ruslan'

'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''
'''
    name = input('enter name')
    surname = input('enter surname')
    age = int(input('enter age'))
    city = input('enter city')
    email = input('enter email')
    telephone = input('input telephone')
'''
def my_func (name, surname, age, city, email, telephone):
    return ' '.join([name, surname, age, city, email, telephone])
print(my_func(surname = 'Molodtsov', name = 'Ruslan', age = '20', city = 'Odessa', email = 'ruha888@mail.ru', telephone = '+38-050-555-55-55'))


