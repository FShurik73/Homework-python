# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

n = int(input("Ведите число: "))  # = 5
my_list = []
sum = 0
for i in range(n):
    my_list.append(random.randint(1, 10))
print(my_list)
for i, x in enumerate(my_list):    # перебирая индексы обращаемся к их значениям
    if i % 2 != 0:
        sum += x 
print(sum, end= ' ')
