# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

n = int(input("Ведите число:> "))  # = 5
my_list = []
summa = 0
for i in range(n):
    my_list.append(random.randint(1, 10))
print(my_list)
for i in range(len(my_list)):    # перебирая индексы обращаемся к их значениям
    if i % 2 != 0:
        summa += my_list[i] 
print(summa)


#---------------------------------------------------------------------------------------------
odd  = [random.randint(1,20) for i in range(int(input("Ведите число:> ")))]
print(odd)

odd  = [x for i, x in enumerate(odd) if i % 2 != 0]
print(sum(odd))


