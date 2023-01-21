# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

def fill_number_list(n=10, min=1, max=10) -> list:
    number_list = [random.randint(min, max)]
    for i in range (1, n):
        number_list.append(random.randint(min, max)) 
    return number_list

def main():
    source_list = fill_number_list()
    print(source_list)
    unique_numbers = []
    for i in source_list:
        if source_list.count(i) == 1:
            unique_numbers.append(i)
    print(unique_numbers)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------
list_num  = [random.randint(1,10) for i in range(10)]
uniq_num = list(filter(lambda x: True if list_num.count(x) == 1 else False, list_num))
print(uniq_num)

