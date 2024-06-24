print('Задача 8. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: При желании найдите описание алгоритма бинарного поиска и попробуйте применить в этой задаче.
#Разбор подобного решения будет в следующем модуле.

print("Загадайте в уме число от 1 до 100 включительно.")
range_start = 1
range_end = 100

tries = 0
while True:
    tries += 1
    guess = (range_end + range_start) // 2

    answer = ""
    while answer == "":
        answer = input("Твоё число равно(1), меньше(3) или больше(2), чем число " + str(guess) + "? ")
        if (answer != "1") and (answer != "2") and (answer != "3"):
            print("Можно отвечать только 1, 2 или 3")
            answer = ""

    if answer == "1":
        print("Вы загадали число ", guess, ", задача решена за ", tries, " шагов.", sep="")
        break
    elif answer == "2":
        range_start = guess
    else:
        range_end = guess
