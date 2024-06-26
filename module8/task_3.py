print('Задача 3. Таймер для микроволновых печей')

# Мы разрабатываем микропрограмму — таймер обратного отсчета для микроволновых печей. Некоторым пользователям не нравится пищащий звук.
# Есть задача убрать звук по готовности и заменить его сообщением на LED-экране. В нашем случае будем выводить в консоль сообщение с обратным отсчетом в секундах от “reverse_timer” до момента готовности, то есть «0» секунд, и спрашивать пользователя, готов ли он забрать еду.

# Пользователь в любой момент может прервать режим разогрева, введя «1» (то есть ответить «Да, еда готова»), тогда программа выводит на экран сообщение «Ваша еда готова, можете забрать» и показывает, на какой секунде был прерван таймер.
# Если пользователь отвечает «0», что равноценно «Нет», то таймер уменьшается. Когда он достигнет «0» секунд, выводим сообщение «Ваша еда готова, осторожно горячo!»

# В данном задании используем цикл for.
# “reverse_timer” – переменная счетчик, значение которой запрашиваем у пользователя через функцию ввода input.

# 1) Задайте время до обнуления таймера.
# 2) Используйте цикл for.
# 3) На каждой итерации задавайте персонажу вопрос, хочет ли он сейчас остановить разогрев или нет.

reverse_timer = int(input("Задайте время до обнуления таймера "))
for second in range(reverse_timer, -1, -1):
    if second == 0:
        print("Ваша еда готова, осторожно горячo!")
    else:
        answer = ""
        while answer == "":
            answer = input(f"Осталось {second} сек, прервать(0) или продолжить(1)? ")
            if (answer != "0") and (answer != "1"):
                print("Можно ввести только 0 или 1")
                answer = ""

        if answer == "0":
            print("Ваша еда готова, можете забрать")
            print(f"Таймер прерван на {second} секунде")
            break
