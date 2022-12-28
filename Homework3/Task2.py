# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Ведите число: "))  # = 5
my_list = []
sum = 0
for i in range(n):
    my_list.append(random.randint(1, 9))
print(my_list)
res = []
for i in range(len(my_list)):                # перебираем список по индексу и значению через разделение пополам
    while i < len(my_list)/2 and n > len(my_list)/2:
        n -= 1
        sum = my_list[i] * my_list[n]
        res.append(sum)
        i += 1
print(res)


from math import ceil

def sum_of_pare(array):
    """
    get list of integer digits and return new list with
    multiplication of elements with elements that has negative some indexes
    :param array: list
    :return: new list
    """
    accumulator = []
    for i in range(ceil(len(array) / 2)):
        accumulator.append(array[i] * array[-(i + 1)])
    return accumulator


print(sum_of_pare([2, 3, 4, 5, 6]))
print(sum_of_pare([2, 3, 5, 6]))

