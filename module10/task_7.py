print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

sym_space = "   "

height = int(input("Введите высоту пирамидки "))
if height < 1:
    print("Пирамидка не получится")
else:
    for row in range(height):
        start_num = (row + 1)**2 - row
        print(sym_space * (height - row - 1), end="")
        for i in range(start_num, start_num + 2*row + 1, 2):
            print(i, sym_space, end="")
        print()
