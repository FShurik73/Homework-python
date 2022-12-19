# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import Random, randint
n = int(input('Введите число: '))
if n < 0:
    n *= -1
num_list = []
for i in range(n):
    num_list.append(randint(-n, n+1))
print(num_list)

a = int(input('Введите позицию для вычисления:> '))
b = int(input('Введите позицию для вычисления:> '))
c = int(input('Введите позицию для вычисления:> '))
pos = open('file.txt', 'w')
pos.write('{}\n'.format(a))
pos.write('{}\n'.format(b))
pos.write('{}\n'.format(c))
pos.close()

pos = open('file.txt', 'r')
result = num_list[int(pos.readline())] * num_list[int(pos.readline(2))]  * num_list[int(pos.readline(3))]
print(f'Произведение указанных прозиций = {result}')

