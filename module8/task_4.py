print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

range_start = int(input("Введите начало интервала (a) "))
range_end = int(input("Введите конец интервала (b) "))
divisor = int(input("Введите делитель (c) "))

correction = range_start % divisor
if correction > 0:
    range_start += divisor - correction

sum = hits = 0
for num in range(range_start, range_end + 1, divisor):
    sum += num
    hits += 1

if hits == 0:
    print("На отрезке нет нужных чисел")
else:
    sum /= hits
    print(f"Ответ: {sum}")
