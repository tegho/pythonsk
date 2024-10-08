print('Задача 4. Простые числа')

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.

# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.

pool_size = int(input("Введите количество чисел: "))
simple_numbers = 0

for counter in range(1, pool_size + 1):
    num = int(input(f"{counter}/{pool_size}) Введите число: "))
    is_simple = 1
    for div in range(2, num):
        if num % div == 0:
            is_simple = 0
            break
    if is_simple == 1:
        simple_numbers += 1

print(f"Количество простых чисел в последовательности: {simple_numbers}")
