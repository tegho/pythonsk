print('Задача 5. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку. Ему особенно понравилась книга «Преступление и наказание». Паоло решил найти самое длинное слово в этой книге, чтобы сравнить его с аналогом на своём языке.

# Что нужно сделать

# Напишите программу, которая получает на вход текст и находит длину самого длинного слова в нём. Слова в тексте разделяются одним пробелом.

# Пример:

# Введите текст: Меня зовут Пётр.
# Самое длинное слово, букв: 5.

# Введите текст: Меня зовут Василий
# Самое длинное слово, 7 букв

longest_len = 0
current_len = 0
separator = " "

text = input("Введите текст: ")
for sym in text + separator:
    if sym != separator:
        current_len += 1
    else:
        if current_len > longest_len:
            longest_len = current_len
        current_len = 0

print(f"Самое длинное слово, букв: {longest_len}")
