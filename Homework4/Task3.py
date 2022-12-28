# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

def fill_number_list(n=10, min=1, max=10) -> list:
    number_list = [random.randint(min, max)]
    for i in range (1, n):
        number_list.append(random.randint(min, max)) 
    return number_list

def main():
    source_list = fill_number_list(10, 1, 10)
    print(source_list)
    unique_numbers = []
    for i in source_list:
        if source_list.count(i) == 1:
            unique_numbers.append(i)
    print(unique_numbers)

if __name__ == '__main__':
    main()