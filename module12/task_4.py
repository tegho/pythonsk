print('Задача 4. Число наоборот')

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
# 
# Введите число: 1000
# Число наоборот: 0001
# 
# Введите число: 0
# Программа завершена!
# 
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
# 
# Введите число: 1230
# Число наоборот: 321
# 
# Кстати, нули, которые мы убрали, называются ведущими.


def reverse_num(num, keep_zeroes):
    string = ""
    leading_zero = True
    while num > 0:
        digit = num % 10
        if leading_zero and (digit != 0):
            leading_zero = False

        if keep_zeroes or (not keep_zeroes and not leading_zero):
            string += str(digit)

        num //= 10

    if keep_zeroes:
        keep_string = "с нулями"
    else:
        keep_string = "без нулей"
    print(f"Число наоборот ({keep_string}): {string}")


def main():
    while True:
        num = int(input("Введите число: "))
        if num == 0:
            print("Программа завершена!")
            break
        elif num < 0:
            print("Число должно быть положительным")
            break
        else:
            reverse_num(num, True)
            reverse_num(num, False)


main()
