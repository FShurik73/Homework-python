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



import random

num = int(input("Ведите число: "))  # = 5
my_list = []
for i in range(num):
    my_list.append(random.randint(-num, num))
print(my_list)
# делали так на 1й задаче 2го семинара

path = 'file.txt'
data = open(path, 'w')
data.write('2\n')
data.write('4\n')
data.close()

path = 'file.txt'
data = open(path, 'r')
mult = 1
for line in data:
    mult*=my_list[int(line)]
    # print(line, end='')
print(mult)


# import random
#
# n = int(input())
# list_num = [random.randint(-n,n) for i in range(n)]
# print(list_num)

file = open("File.txt","r")
multi = 1
list_str = file.readlines()
print(list_str)
list_num = list(map(str.strip,list_str))
print(list_num)
list_num = list(map(int,list_num))
print(list_num)
for i in file:
    multi*=list_num[int(i)]
print(multi)

