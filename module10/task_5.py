print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

pool_size = counter = int(input("Сколько будет чисел в ряду? "))
max_sum = 0
max_num = 0

if pool_size < 1:
    print("Нет, этого мало")
else:
    for counter in range(1, pool_size + 1):
        num = n = int(input(f"{counter}/{pool_size}) Введите число "))
        sum = 0
        while (n > 0):
            sum += n % 10
            n //= 10
        if sum > max_sum:
            max_sum = sum
            max_num = num
    if max_num < 1:
        print("Натуральных чисел в ряду не нашлось")
    else:
        print(f"Натуральное число {max_num} имеет максимальную сумму цифр {max_sum}")
