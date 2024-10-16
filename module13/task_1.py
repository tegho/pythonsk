print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
# 
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
# 
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
# 
# Пример 1:
# 
# Введите число: 92345
# 
# Формат плавающей точки: x = 9.2345 * 10 ** 4
# 
# Пример 2:
# 
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

x = float(input("Введите значение X: "))
if x <= 0:
    print("Х должен быть больше нуля")
    exit()

mult = 0.1
dir = 1
if x < 1:
    mult = 10
    dir = -1

significand = x
exponent = 0
while (int(significand) not in range(1, 10)):
    significand *= mult
    exponent += dir

# мантиссу вычисляем повторно чтобы избавиться от накопленной ошибки
significand = x / (10 ** exponent)

print(f"Формат плавающей точки: x = {significand} * 10 ** {exponent}")
