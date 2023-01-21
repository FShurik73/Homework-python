# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.    
#     *Пример:*   
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Print your N: '))
# my_dict = {}

# for i in range(1,n+1):
#     my_dict[i] = 3*i + 1
# print(my_dict)
#-----------------------------------------------------------------

my_list = [i for i in range(1, int(input('Введите число:> ')) + 1)]
new_list = [3*i + 1 for i in range(1, len(my_list) + 1)]
my_dict = dict(zip(my_list,new_list))
print(my_dict)



