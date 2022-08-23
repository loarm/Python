from random import randint
import pdb
import sys


def getMax():
    while True:
        try:
            print('Enter a max number of the range: ')
            max_int = int(input())
            return max_int
        except:
            print('Please enter a number!')
        finally:
            print()
            print(f'Your range numbers to guess are 1-{max_int}')
            print()


def getGuess(max_int):
    while True:
        try:
            print('Make your guess: ')
            guess = int(input())
            return guess
        except:
            print()
            print(f'Please enter a number between 1 and {max_int}')
            print()


def GuessingGame():
    # pdb.set_trace()
    print('Hello! You\'re playing a GuessingGame. \nChoose the maximum number of the range and try to guess it. \nYou have only 7 tries, so make your guess wisely. Good luck!')
    print()

    max_int = getMax()

    number = randint(1, max_int)
    guesses = set()
    tries = 7

    while True:
        guess = getGuess(max_int)

        if 1 <= tries <= 7:
            if guess != number:
                if guess < number:
                    print(
                        f'Your guess _{guess}_ is lower. Try again! \nNumber of tries left: {tries}')
                    if tries < 7:
                        print(f'Previous guesses: {guesses}')
                    print()
                    guesses.add(guess)
                    tries -= 1
                    continue
                elif guess > number:
                    print(
                        f'Your guess _{guess}_ is higher. Try again! Number of tries left: {tries}')
                    if tries < 7:
                        print(f'Previous guesses: {guesses}')
                    print()
                    guesses.add(guess)
                    tries -= 1
                    continue
            elif guess == number:
                print(
                    f'Yeeeeh! You guessed it! Your number is "{number}". \nYou guessed from the {8 - tries} try. \nDo you want to play again? (y/n)')
                if input() in ('yes y'.split()):
                    GuessingGame()
                    continue
                else:
                    print('See ya next time! Bye:)')
                    break
        else:
            print(
                f'Sorry, you\'ve run out of tries :( Your number was "{number}" \nDo you want to try again? (y/n)')
            if input() in ('yes y'.split()):
                GuessingGame()
                continue
            else:
                print('See ya next time! Bye:)')
                break


if __name__ == '__main__':
    GuessingGame()
