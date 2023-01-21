# def pvp():
#     name1 = input("Введите имя первого игрока - ")
#     name2 = input("Введите имя второго игрока - ")
#     sweets = int(input("Введите желаемое колчиество конфет - "))
#     max_sweet = int(input("Введите максимум конфет за ход"))
#
#     first_turn = random.choice([name1,name2])
#
#     flag = name1 if first_turn == name1 else name2
#
#     while sweets>0:
#         print(f"Ваш ход {flag}")
#
#         turn = int(input("введите желаемое количество конфет для взятия- "))
#
#         while not 0 < turn <= max_sweet:
#             print("Введите конфеты в диапазоне от 0 до", max_sweet)
#             turn = int(input("введите желаемое количество конфет для взятия- "))
#         if sweets > 0:
#                 print(f'конфет осталось - {sweets}')
#         else:
#             print(f'конфет осталось - 0')
#
#         flag = name2 if flag == name1 else name1
#
#     winner = name2 if flag == name1 else name1
#     print(f"Поздравляем победил игрок {winner}")
# def pve_st():
#     name1 = input("Введите имя первого игрока - ")
#     name2 = "bot"
#     sweets = int(input("Введите желаемое колчиество конфет - "))
#     max_sweet = int(input("Введите максимум конфет за ход - "))
#
#     first_turn = random.choice([name1, name2])
#
#     flag = name1 if first_turn == name1 else name2
#
#     while sweets>0:
#         print(f"Ваш ход {flag}")
#         if flag == name1:
#             turn = int(input("введите желаемое количество конфет для взятия- "))
#
#             while not 0 < turn <= max_sweet:
#                 print("Введите конфеты в диапазоне от 0 до", max_sweet)
#                 turn = int(input("введите желаемое количество конфет для взятия- "))
#             sweets -= turn
#
#             if sweets > 0:
#                     print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')
#
#             flag = name2 if flag == name1 else name1
#         else:
#             turn = random.randint(1,max_sweet)
#             print(f"bot взял {turn} конфет")
#             sweets -= turn
#             if sweets > 0:
#                     print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')
#             flag = name2 if flag == name1 else name1
#
#     winner = name2 if flag == name1 else name1
#     print(f"Поздравляем победил игрок {winner}")
# def pve_smart():
#     name1 = input("Введите имя первого игрока - ")
#     name2 = "bot"
#     sweets = int(input("Введите желаемое колчиество конфет - "))
#     max_sweet = int(input("Введите максимум конфет за ход - "))
#
#     first_turn = random.choice([name1, name2])
#
#     flag = name1 if first_turn == name1 else name2
#
#     while sweets>0:
#         print(f"Ваш ход {flag}")
#         if flag == name1:
#             turn = int(input("введите желаемое количество конфет для взятия- "))
#
#             while not 0 < turn <= max_sweet:
#                 print("Введите конфеты в диапазоне от 0 до", max_sweet)
#                 turn = int(input("введите желаемое количество конфет для взятия- "))
#
#             sweets -= turn
#
#             if sweets > 0:
#                     print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')
#             flag = name2 if flag == name1 else name1
#         else:
#             if sweets == max_sweet:
#                 turn = max_sweet
#             elif sweets%max_sweet==0:
#                 turn = max_sweet-1
#             else:
#                 turn = sweets%max_sweet-1
#             print(f"bot взял {turn} конфет")
#             sweets -= turn
#             if sweets > 0:
#                     print(f'конфет осталось - {sweets}')
#             else:
#                 print(f'конфет осталось - 0')
#             flag = name2 if flag == name1 else name1
#
#     winner = name2 if flag == name1 else name1
#     print(f"Поздравляем победил игрок {winner}")
# pve_smart()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------











