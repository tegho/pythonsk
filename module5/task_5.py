print('Задача 5. Вася хочет выигрывать')

# Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов. Для анализа данных ему нужна информация о том, как часто в автомате выпадает три или две одинаковых картинки. Для сбора данных нужна программа, проверяющая это равенство. 

# Даны три целых числа. Определите, сколько среди них совпадающих. 
# Программа должна вывести один из вариантов: 
# 1) 3 (если все совпадают) 
# 2) 2 (если два совпадают)
# 3) 0 (если все числа разные)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 == num2:
    same = 2
    if num3 == num1:
        same += 1
elif num1 == num3:
    same = 2
    if num2 == num1:
        same += 1
elif num2 == num3:
    same = 2
    if num1 == num2:
        same += 1
else:
    same = 0

print("Совпадений:", same)
