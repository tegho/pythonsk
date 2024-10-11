import random

print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
    """ Игра "Камень, ножницы, бумага" """
    options_list = ["КАМЕНЬ", "БУМАГА", "НОЖНИЦЫ"]
    while True:
        command = input("\nИграем в КНБ. Введите строкой:\n  камень\n  ножницы\n  бумага\n  Q чтобы выйти\n").upper()
        if (command not in options_list) and (command != "Q"):
            print("Нет такого варианта")
            continue

        if command == "Q":
            break
        else:
            computer_bid = random.randrange(len(options_list))
            user_bid = options_list.index(command)
            print(f"Компьютер: {options_list[computer_bid]}, вы: {command})")
            if computer_bid == user_bid:
                print("Ничья")
            elif (computer_bid + 1 == user_bid) or ((computer_bid + 1 >= len(options_list)) and (user_bid == 0)):
                print("Вы выиграли")
            else:
                print("Компьютер выиграл")


def guess_the_number():
    """ Игра "Угадай число" """
    NUM_TRIES = 3
    MAX_NUM = 9
    print("\nИграем в угадай число")
    keep_playing = True
    while keep_playing:
        computer_bid = random.randrange(MAX_NUM + 1)
        print(f"\nКомпьютер загадал целое от 0 до {MAX_NUM} включительно. Угадайте с {NUM_TRIES} попыток. Q - выход (ПОДСКАЗКА: {computer_bid})")
        for guess_try in range(1, NUM_TRIES + 1):
            command = input(f"{guess_try}/{NUM_TRIES}) Ваше число: ").upper()
            if command == "Q":
                keep_playing = False
                break
            user_bid = int(command)
            if user_bid != computer_bid:
                print("Нет")
            else:
                print("Правильно!\nВы выиграли")
                break
        else:
            print("Компьютер выиграл")


def main_menu():
    """ Главное меню игры """
    options_list = ["Q", "1", "2"]
    while True:
        command = input(f"\nЧто будем делать?\n  Q - выход из программы\n  1 - Играть в КНБ\n  2 - Играть в угадай число\n").upper()
        if command not in options_list:
            print("Неизвестная команда")
            continue

        if command == "Q":
            break
        elif command == "1":
            rock_paper_scissors()
        elif command == "2":
            guess_the_number()
        else:
            print("Для этой команды забыли написать обработчик")


main_menu()
