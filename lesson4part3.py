__author__ = 'Molodtsov Ruslan'

'''
Представлен список чисел. Определить элементы списка,
не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести
в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
'''

my_list = [5, 8, 8, 6, 7, 6, 10, 12, 10, 18]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)