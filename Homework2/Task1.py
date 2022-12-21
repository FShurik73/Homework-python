# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите число: ')

def summa(num):                            #Функция нахождения суммы чисел в заданном числе
    #if float(num) < 0:                            #Проверка на знак перед числом
    num = abs(float(num))# * (-1)
    number = 0

    for i in str(num):
        if i != '.':
            number += int(i)
    return number   
print(f'Сумма числа {num} равна {summa(num)}')


def summa1(num):      #Функция нахождения суммы чисел в заданном числе
    number = 0
    for i in str(num):
        if i.isdigit():
            number += int(i)
    return number

print(f'Сумма числа {num} равна {summa1(num)}')

#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input()
# summ = 0
# for i in n:
#     if i.isdigit():
#         summ+=int(i)
# print(summ)


# n = float(input())
# len_num = len(str(n))-1
# summ=0
# while n!=int(n):
#     n= round(n*10,len_num)
#     print(n)
# while n>0:
#     summ+=n%10
#     n = n//10
# print(summ)
