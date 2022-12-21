# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random

n = int(input("Ведите число: "))  
my_list = []
sum = 0
for i in range(n):                 # создаем рандомный список вещественных чисел
    my_list.append(random.uniform(1, 9))
res = []
for i, x in enumerate(my_list): 
    x = x % 1
    res.append(x)
form_res = [round(elem, 2) for elem in res ]   # округляем значения списка до сотых
print(form_res)
diff = (max(form_res)) - (min(form_res))
print(f'Разница между максимальным {max(form_res)} и мииимальным {min(form_res)} значением дробной части = {diff}')

