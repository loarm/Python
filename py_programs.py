# Имитация бросания игральных кубиков.
# Программа должна случайным образом генерировать два числа в диапазоне от 1 до 6 и показывать их.
from random import *

def dice_gen():
    again = 'y'
    while again.lower() == 'y':
        print('Бросаем кубик...')
        print(f'Значение граней {randint(1, 6)} и {randint(1, 6)}')
        print()
        again = input('Бросить кубики ещё раз? (y = да, n = нет)')

def heads_n_tails():

    again = 'y'
    while again.lower() == 'y':
        print('Бросаем монетку...')
        [print(('Решка', 'Орел') [__import__('random').randint(0, 1)]) for _ in range(1)]
        again = input('Бросить монетку ещё раз? (y = да, n = нет)')


print("Программы", "1. Подбросить кубик", "2. Подросить монетку", sep="\n")
print()
choice = input("Выберите программу для запуска: 1 или 2")

if choice == '1':
    dice_gen()
else:
    heads_n_tails()