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

