# Сформировать список из N членов последовательности
#Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

n = int(input())
symbol = 1
print(symbol, end = " ")
for i in range(n-1):
    symbol *= -3
    print(symbol, end = " ")
print()

#-------------------------------------------------------------------------------------------------

my_list = [i for i in range( int(input("Ведите число:> ")))]
my_list = [(-3) ** i for i in my_list]
print(my_list)
