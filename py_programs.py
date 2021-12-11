from random import *


# Программа случайным образом генерирует два числа в диапазоне от 1 до 6
def dice_gen():
    again = 'y'
    while again.lower() == 'y':
        print('Бросаем кубик...')
        print(f'Значение граней {randint(1, 6)} и {randint(1, 6)}')
        print()
        again = input('Бросить кубики ещё раз? (y = да, n = нет) ')
    if again == 'n':
        return start()


# Программа имитации подбрасывания монетки с результатом Орел и Решка.
def heads_n_tails():
    again = 'y'
    while again.lower() == 'y':
        print('Бросаем монетку...')
        print(*[('Решка', 'Орёл')[randint(0, 1)] for _ in range(1)])
        again = input('Бросить монетку ещё раз? (y = да, n = нет) ')
    if again == 'n':
        return start()


# проверка валидности введенного числа
def is_valid(num):
    num = int(num)
    if 1 <= num <= 100:
        return True
    else:
        return False


# программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число
def guess_num():
    num = randint(1, 101)
    counter = 0
    while True:
        user = input("Загадайте число от 1 до 100 ")
        if not is_valid(user):
            print("Введите целое число от 1 до 100!")
            continue
        user = int(user)
        if user < num:
            print(f"Число {user} слишком маленькое, попробуйте ещё раз")
            counter += 1
        if user > num:
            print(f"Число {user} слишком большое, попробуйте ещё раз")
            counter += 1
        if user == num:
            print(f"Вы угадали - число {num}, поздравляем! Количество попыток {counter}.")
            print()
            print("Хотите сыграть ещё раз?")
            if input() == 'y':
                print()
                continue
            else:
                print()
                return start()


# магический шар с 20 вариантами ответов
def prediction():

    answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
               "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
               "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
               "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
    print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
    name = input("Как тебя зовут? ")
    print(f"Привет, {name}!")

    while True:
        q = input("Что ты хочешь знать? Задай свой вопрос: ")
        if not q == '':
            print(choice(answers))
        else:
            continue
        q = input("У тебя ещё остались вопросы? (y = да, n = нет) ")
        if q == 'n':
            print("Возвращайся если возникнут вопросы!")
            return start()
            #break
        else:
            continue

# программа генерации пароля
def generate_password():
    custom = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!#$%&*+-=?@^_']
    chars = ''
    n = int(input("Введите количество генерируемых паролей: "))
    lenth = int(input('Введите длину пароля: '))

    if lenth < 8:
        print("Пароль короче 8 символов может быть небезопасным. Вы уверены, что хотите продолжить?  (y = да, n = нет)")
        if input() == 'n':
            lenth = int(input('Введите длину пароля: '))
    for i in range(len(custom)):
        p = input(f'Включать ли {custom[i]} в пароль? (y = да, n = нет) ')
        if p == 'y':
            chars += ''.join(custom[i])
    for _ in range(1, n + 1):
        pas = sample(chars, lenth)
        print("Ваш пароль ", *pas, sep='')
    print("Хотите продолжить? (y = да, n = нет)")
    if input() == 'n':
        return start()
    else:
        generate_password()

# app boot
def start():
    print("Программы", "1. Подбросить кубик", "2. Подросить монетку", "3. Угадайка число!", "4. Магический шар 8", "5. Генератор паролей",
          sep="\n")
    print()
    order = input("Введите номер программы для запуска: ")
    if order == '1':
        dice_gen()
    elif order == '2':
        heads_n_tails()
    elif order == '3':
        guess_num()
    elif order == '4':
        prediction()
    elif order == '5':
        generate_password()




if __name__ == '__main__':
    start()


