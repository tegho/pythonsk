print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. 
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру. 

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


def sum_digits(num):
    num = abs(num)
    summa = 0
    while num > 0:
        summa += num % 10
        num //= 10
    print(f"Сумма цифр: {summa}")


def max_digit(num):
    num = abs(num)
    max_digit = 0
    while num > 0:
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
        num //= 10
    print(f"Максимальная цифра: {max_digit}")


def min_digit(num):
    num = abs(num)
    min_digit = 9
    while num > 0:
        digit = num % 10
        if digit < min_digit:
            min_digit = digit
        num //= 10
    print(f"Минимальная цифра: {min_digit}")


def main():
    while True:
        num = int(input("\nВведите число "))

        command = ""
        while command == "":
            command = input(f"\nЧисло: {num}\nВыберите команду:\n  Q - выход\n  S - сумма цифр\n  H - максимальная цифра\n  L - минимальная цифра\n").upper()
            if command not in "QSLH":
                print("Неизвестная команда")
                command = ""

        if command == "Q":
            break
        elif command == "S":
            sum_digits(num)
        elif command == "H":
            max_digit(num)
        elif command == "L":
            min_digit(num)
        else:
            print("Для этой команды забыли написать обработчик")


main()
