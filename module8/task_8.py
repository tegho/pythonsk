print('Задача 8. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBBGBBG
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

boys = int(input("Введите количество мальчиков: "))
girls = int(input("Введите количество девочек: "))
res = ""

min_of = min(boys, girls)
max_of = max(boys, girls)
diff = max_of - min_of
if (min_of == 0) or (max_of / min_of > 2):
    res = "Нет решения"
else:
    if boys >= girls:
        k = boys - girls
        for bgb in range(k):
            res += "BGB"
        for bg in range(girls - k):
            res += "BG"
    else:
        k = girls - boys
        for gbg in range(k):
            res += "GBG"
        for gb in range(boys - k):
            res += "GB"
print(f"Ответ: {res}")
