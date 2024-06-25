print('Задача 7. Метод бутерброда')

# В секретном агентстве Super-Secret-no решили использовать «метод бутерброда» для шифрования переписки своих сотрудников. Сначала буквы слова нумеруются в таком порядке: первая буква получает номер 1, последняя буква — номер 2, вторая — номер 3, предпоследняя — номер 4, потом третья… и так для всех букв (см. рисунок). Затем все буквы записываются в шифр в порядке своих номеров.

# Например, слово «sandwich» зашифруется в «shacnidw».
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.

# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
# Шифр:  | s | h | a | c | n | i | d | w |

encrypted_text = input("Введите зашифрованное сообщение: ")
text_left = text_right = ""

for pos, sym in enumerate(encrypted_text):
    if pos % 2 == 0:
        text_left += sym
    else:
        text_right = sym + text_right

print(f"Расшифрованное сообщение: {text_left + text_right}")
