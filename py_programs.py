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
        print(*[('Решка', 'Орел')[randint(0, 1)] for _ in range(1)])
        again = input('Бросить монетку ещё раз? (y = да, n = нет) ')
    if again == 'n':
        return start()


# программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число
def guess_num():
    pass


# app boot
def start():
    print("Программы", "1. Подбросить кубик", "2. Подросить монетку", "3. Угадайка число!", sep="\n")
    print()
    choice = input("Введите номер программы для запуска: ")


# MAIN
start()
games = {'1': dice_gen(), '2': heads_n_tails(), '3': guess_num()}
print(games(choice))
