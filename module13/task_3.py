print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225


def input_is_good(str_input):
    """ FALSE if any symbols other than 0-9 present """
    # вместо try-catch проверим ввод разбором строки
    ALLOWED_SYMBOLS = "1234567890"
    if len(str_input) < 1:
        print("Пустая строка\n")
        return False
    for next_sym in str_input:
        if ALLOWED_SYMBOLS.find(next_sym) < 0:
            print("Недопустимые символы\n")
            return False
    return True


def str_reverse_to_int(source_str):
    """ Переворачивает строку и преобразовывает в int """
    rev_str = ""
    for sym in source_str:
        rev_str = sym + rev_str
    return int(rev_str)


def int_reverse_to_str(num):
    """ Преобразовывает int в строку и переворачивает """
    source_str = str(num)
    rev_str = ""
    for sym in source_str:
        rev_str = sym + rev_str
    return rev_str


str1 = ""
str2 = ""
while True:
    str1 = input("Введите первое число: ")
    if input_is_good(str1):
        break

while True:
    str2 = input("Введите второе число: ")
    if input_is_good(str2):
        break

num1 = str_reverse_to_int(str1)
num2 = str_reverse_to_int(str2)
summa = num1 + num2
print(f"\nПервое число наоборот: {num1}")
print(f"Второе число наоборот: {num2}")
print(f"Сумма: {summa}")
print(f"\nСумма наоборот: {int_reverse_to_str(summa)}")
