print("Задача 6. Пирамидка")


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


   #
  ###
 #####
#######
sym_space = " "
sym_pyramid = "#"

height = int(input("Введите высоту пирамидки "))
if height < 1:
    print("Пирамидка не получится")
else:
    for row in range(height):
        # # можно обойтись без вложенных циклов
        # print(f"{sym_space * (height - row - 1)}{sym_pyramid * (row * 2 + 1)}")

        # или с циклом
        for col in range(2 * height - 1):
            if col < height - row - 1:
                print(sym_space, end="")
            elif col < height + row:
                print(sym_pyramid, end="")
            else:
                # можно заполнить строку до конца, но необязательно
                print(sym_space, end="")
        print()
