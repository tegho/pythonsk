print('Задача 4. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу. Однако старший программист попросил вас немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.

# Постарайтесь разделить логику кода на три отдельные логические части (функции):
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.


def count_numbers(num):
    if num == 0:
        return 1

    counter = 0
    while num > 0:
        num //= 10
        counter += 1
    return counter


def change_number(num):
    counter = count_numbers(num)
    last_digit = num % 10
    first_digit = num // (10 ** (counter - 1))
    between_digits = (num % (10 ** (counter - 1))) // 10
    return last_digit * 10 ** (counter - 1) + between_digits * 10 + first_digit


def user_input(msg, digits):
    num = int(input(msg))
    if count_numbers(num) < digits:
        print(f"Не менее {digits} цифр")
        return -1
    return num


def main():
    num1 = user_input("\nВведите первое число: ", 3)
    if num1 < 0:
        return
    num1_new = change_number(num1)
    print(f"Изменённое первое число: {num1_new}")

    num2 = user_input("\nВведите второе число: ", 4)
    if num2 < 0:
        return
    num2_new = change_number(num2)
    print(f"Изменённое второе число: {num2_new}")

    summa = num1_new + num2_new
    print(f"\nСумма чисел: {summa}")


main()
