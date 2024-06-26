print('Задача 1. Должники')

# В базе банка хранятся данные и должников, и законопослушных граждан. Каждому человеку система присваивает свой номер. У нас есть случайная выборка из десяти номеров. Правда, иногда база глючит и выдаёт номер с отрицательным значением. А ещё по статистике, которую собрал наш «МирПрогБанк», каждый второй пользователь брал кредит и не выплатил его вовремя, то есть является должником.

# Напишите программу, которая при вводе десяти чисел определяет, сколько из них являются одновременно чётными и положительными.

pool_size = 10
for person in range(1, pool_size + 1):
    num = int(input(f"{person}/{pool_size}) Введите число "))
    if (num % 2 == 0) and (num >= 0):
        print("  Четное положительное.")
