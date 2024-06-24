import random

print('Задача 7. Игра «Угадай число»')

# В одной из практических работ мы делали задачу, где папа-программист написал для сына программу, которая просит его угадать число. Недостаток программы был в том, что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно немного улучшить саму игру.

# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.

# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4

father_num = random.randint(1, 9)

tries = 1
while True:
    num = int(input("Введите число: "))
    if num > father_num:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif num < father_num:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали! Число попыток:", tries)
        break
    tries += 1
