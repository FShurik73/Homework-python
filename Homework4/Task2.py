# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число:> "))

def prime_factors(n):
    i = 2           # первое простое число
    primfac = []
    while i <= n:
        if n % i == 0:
            primfac.append(i)
            n //= i
            i = 2
        else:
            i += 1
    return primfac
print(prime_factors(n))



