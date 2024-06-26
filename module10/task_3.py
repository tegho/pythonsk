print('Задача 3. Рамка')

# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|


# Текст расходится с примером. Скорректируем задачу ближе к тексту, добавим углы
# +------+
# |      |
# |      |
# +------+
# Минимальный
# +-+
# | |
# +-+
sym_horiz = "-"
sym_vert = "|"
sym_corner = "+"
sym_space = " "

width = int(input("Введите ширину "))
heigh = int(input("Введите высоту "))

if (width < 3) or (width > 80) or (heigh < 3) or (heigh > 25):
    print("Недопустимые размеры")
else:
    # можно обойтись без вложенного цикла
    # for row in range(heigh):
    #     if (row == 0) or (row == heigh - 1):
    #         print(sym_corner, sym_horiz * (width - 2), sym_corner, sep="")
    #     else:
    #         print(sym_vert, sym_space * (width - 2), sym_vert, sep="")

    # а можно с циклом
    for row in range(heigh):
        for col in range(width):
            if (col == 0) or (col == width - 1):
                if (row == 0) or (row == heigh - 1):
                    print(sym_corner, end="")
                else:
                    print(sym_vert, end="")
            else:
                if (row == 0) or (row == heigh - 1):
                    print(sym_horiz, end="")
                else:
                    print(sym_space, end="")
        print()
    #
