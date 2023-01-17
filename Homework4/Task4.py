# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: 
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def write_file(st):                         # функция записи в файл
    with open('Task4.txt', 'w') as data:
        data.write(st)

def rnd():                                  # функция создания рандомных чисел от 0 до 100
    return random.randint(0, 101)

def create_mn(k):                           # функция списка рандомных чисел
    lst = [rnd() for i in range(k+1)]
    return lst

def create_str(sp):
    polinom = sp[::-1]                           # переворот списка
    wr = ''
    if len(polinom) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(polinom)):
            if i != len(polinom) - 1 and polinom[i] != 0 and i != len(polinom) - 2:     #запись многочлена со степенями
                wr += f'{polinom[i]}x^{len(polinom)-i-1}'
                if polinom[i+1] != 0:
                    wr += ' + '                                                        
            elif i == len(polinom) - 2 and polinom[i] != 0:                             # запись х без степени
                wr += f'{polinom[i]}x'
                if polinom[i+1] != 0:
                    wr += ' + '
            elif i == len(polinom) - 1 and polinom[i] != 0:                             # запись числа
                wr += f'{polinom[i]} = 0'
            elif i == len(polinom) - 1 and polinom[i] == 0:                             # равность нулю
                wr += ' = 0'
    return wr

def main():
    k = int(input("Введите натуральную степень k = "))
    koef = create_mn(k)
    write_file(create_str(koef))

if __name__ == '__main__':
    main()




# Второй вариант
import random
from os import system

system("cls")

k = int(input('Enter degree of number: '))

polynominal = ''
for i in range(k, 0, -1):
    polynominal += str(random.randrange(0,101))+'*x^' + str(i) + ' + '
polynominal += str(random.randrange(0,101)) + ' = 0'
print(polynominal)

with open('polynominal.txt', "w") as f_obj:
    print(polynominal, file=f_obj, end='')


# 3

import random
from os import system

system("cls")

k = int(input('Enter degree of number: '))

polynominal = ''
for i in range(k, 1, -1):
    new_k = random.randrange(0,101)
    if new_k > 1:
        polynominal += str(new_k)+'*x^' + str(i) + ' + '
    elif new_k == 1:
        polynominal += 'x^' + str(i) + ' + '
        
new_k = random.randrange(0,101)
if new_k > 1:
    polynominal += str(new_k)+'*x'
elif new_k == 1:
    polynominal += 'x'
    
new_k = random.randrange(0,101)
if new_k:
    polynominal += ' + ' + str(new_k) + ' = 0'
else:
    polynominal += ' = 0'
    
print(polynominal)
