#  Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
a = input('Введите дробное число с заданной точностью d:> ')
d = a[a.find('.')+1:]
count = 0
for i in range(len(d)):
    count += 1
print(f'число Пи с заданной точностью {count} равно {round(pi, count)}')
