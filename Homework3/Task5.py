#  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных
# индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = int(input("Ведите число: "))
def get_fibonacci(n):
    fibo_list = []
    a, b = 1, 1
    for i in range(n):
        fibo_list.append(a)
        a, b = b, a + b
    a, b = 0, 1   
    for i in range (n + 1):
        fibo_list.insert(0, a)
        a, b = b, a - b
    return fibo_list
print(get_fibonacci(n))


def fib(n):
    fib_list = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        fib_list.append(x)
        fib_list.insert(0, -x if i %2 else x)
    return fib_list

fib_num = int(input('Input number: '))
print(f'для k = {fib_num} список будет выглядеть так: {fib(fib_num)}')
