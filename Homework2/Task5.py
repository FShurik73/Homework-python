# Реализуйте алгоритм перемешивания списка.

from random import Random, randint

N = int(input('Введите число '))
numbers = []
for i in range(N):
    numbers.append(randint(-50,50))
print(numbers)

def smesh(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = randint(0, numbers_length)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(smesh(numbers))



import random


def list_shuffle(_list: list):
    shuffled_list = []
    temp_list = _list

    for _ in range(len(_list)):
        position = random.randint(0, len(temp_list) - 1)
        shuffled_list.append(temp_list.pop(position))
    return shuffled_list


print(list_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

import datetime
def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6
    return int(num*rand)

a = [1,2,3,4,5,6]
print(a)
random_int(5)
for i in range(len(a)-1,-1,-1):
    j = random_int(i+1)
    a[i],a[j] = a[j],a[i]
print(a)
