print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

num = int(input("Введите число "))
for row in range(num):
    for col in range(num):
        if col <= row:
            print(row + 1, end="\t")
        else:
            break
    print()
