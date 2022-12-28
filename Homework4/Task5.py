# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def write_file(name, st):                           # запись в файл
    with open(name, 'w') as data:
        data.write(st)

def create_str(sp):                                  # создание многочлена в виде строки
    polinom = sp[::-1]
    wr = ''
    if len(polinom) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(polinom)):
            if i != len(polinom) - 1 and polinom[i] != 0 and i != len(polinom) - 2:
                wr += f'{polinom[i]}x^{len(polinom)-i-1}'
                if polinom[i+1] != 0 or polinom[i+2] != 0:
                    wr += ' + '
            elif i == len(polinom) - 2 and polinom[i] != 0:
                wr += f'{polinom[i]}x'
                if polinom[i+1] != 0 or polinom[i+2] != 0:
                    wr += ' + '
            elif i == len(polinom) - 1 and polinom[i] != 0:
                wr += f'{polinom[i]} = 0'
            elif i == len(polinom) - 1 and polinom[i] == 0:
                wr += ' = 0'
    return wr

def sq_mn(k):                                                # получение степени многочлена
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def k_mn(k):                                                  # получение коэффицента члена многочлена
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def calc_mn(str):                                                # разбор многочлена и получение его коэффициентов
    str = str[0].replace(' ', '').split('=')
    str = str[0].split('+')
    polinom = []
    l = len(str)
    k = 0
    if sq_mn(str[-1]) == -1:
        polinom.append(int(str[-1]))
        l -= 1
        k = 1
    i = 1               # степень
    ii = l-1            # индекс
    while ii >= 0:
        if sq_mn(str[ii]) != -1 and sq_mn(str[ii]) == i:
            polinom.append(k_mn(str[ii]))
            ii -= 1
            i += 1
        else:
            polinom.append(0)
            i += 1

    return polinom

with open('Task5.1.txt', 'r') as data:
    str1 = data.readlines()
print(f"Первый многочлен {str1}")
with open('Task5.2.txt', 'r') as data:
    str2 = data.readlines()
print(f"Второй многочлен {str2}")
polinom1 = calc_mn(str1)
polinom2 = calc_mn(str2)
ll = len(polinom1)
if len(polinom1) > len(polinom2):
    ll = len(polinom2)
polinom_new = [polinom1[i] + polinom2[i] for i in range(ll)]
if len(polinom1) > len(polinom2):
    mm = len(polinom1)
    for i in range(ll, mm):
        polinom_new.append(polinom1[i])
else:
    mm = len(polinom2)
    for i in range(ll, mm):
        polinom_new.append(polinom2[i])
write_file("Task5_res.txt", create_str(polinom_new))
with open('Task5_res.txt', 'r') as data:
    str3 = data.readlines()
print(f"Результирующий многочлен {str3}")

