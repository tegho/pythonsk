print('Задача 5. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)

range_start = int(input("Введите одно число "))
range_end = int(input("Введите другое число "))

if range_start > range_end:
    range_start, range_end = range_end, range_start

res = hits = 0
for num in range(range_start, range_end + 1):
    if num % 3 == 0:
        hits += 1
        res += num
if hits > 0:
    res /= hits
    print("Ответ:", res)
else:
    print("Чисел кратных 3 на отрезке нет")
