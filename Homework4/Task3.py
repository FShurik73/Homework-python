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
#s=input()
#print(s.isdigit.count())

# Второй вариант
# def row_without_repeatitions(row: list) -> list:
#     sieve = {}
#     clean_row = []
#     for i in row:
#         if i in sieve:
#             sieve[i] += 1
#         else:
#             sieve.setdefault(i, 0)
#     for key, value in sieve.items():
#         if not value:
#             clean_row.append(key)

#     return clean_row


# if __name__ == '__main__':
#     row = [random.randint(1, 8) for _ in range(10)]
#     print(row)
#     print(row_without_repeatitions(row))
