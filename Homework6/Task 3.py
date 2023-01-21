# Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

from math import ceil
import random

n = int(input("Ведите число:> "))  # = 5
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

#------------------------------------------------------------------------------------------
my_list = [random.randint(1,20) for i in range(int(input("Ведите число:> ")))]
print(my_list)

res = [(my_list[i] * my_list[-(i + 1)]) for i in range(ceil(len(my_list) / 2))]
print(res)