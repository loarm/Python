from random import *


# Программа должна случайным образом генерировать два числа в диапазоне от 1 до 6 и показывать их
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


# программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число
def guess_num():
    # again = 'n'
    num = randint(1, 100)
    while True:
        user = int(input("Загадайте число от 1 до 100 "))
        if user > num:
            print(f"Число {user} слишком большое, попробуйте еще раз")
        if user < num:
            print(f"Число {user} слишком маленькое, попробуйте еще раз")
        if user == num:
            print(f"Вы угадали, поздравляем! Число {num}!")
            print()
            print("Хотите сыграть ещё раз?")
            if input() == 'y':
                print()
                continue
            else:
                print()
                return start()


# app boot
def start():
    print("Программы", "1. Подбросить кубик", "2. Подросить монетку", "3. Угадайка число!", sep="\n")
    print()
    global choice
    choice = input("Введите номер программы для запуска: ")
    if choice == '1':
        dice_gen()
    elif choice == '2':
        heads_n_tails()
    elif choice == '3':
        guess_num()


# MAIN

start()
