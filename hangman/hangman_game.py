'''
Программа загадывает слово, а пользователь должен его угадать.
Изначально все буквы слова неизвестны. Также рисуется виселица с петлей.
Пользователь предлагает букву, которая может входить в это слово.
Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове.
Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову.
Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово.
За каждую неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги.
'''

import random
import string


from hangman.hangman_visual import hangman_dict
from words import WORDLIST


def get_word():
    word = random.choice(WORDLIST).upper()
    return word.upper()


def is_valid(letter):
    alphab = set(string.ascii_uppercase)
    if letter in alphab:
        return True
    else:
        return False



def play_game():
    word = get_word()
    word_letters = set(word)
    used_letters = set()  # what user has used
    alphab = set(string.ascii_uppercase)

    lives = 6  # number of tries

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f"You have {lives} lives left and you have used these letters: ", ' '.join(used_letters))

        # current word
        word_completion = [letter if letter in used_letters else "-" for letter in
                           word]  # string with guessed letters and hidden inguessed letters
        print(hangman_dict[lives])
        print("Current word: ", ' '.join(word_completion))

        # getting user input
        print("Guess a letter..")
        guess = input().upper()
        if guess in alphab - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1  # player loses 1 life
        elif guess in used_letters:
            print("You already used it. Try again.")
        elif not is_valid(guess):
            print("Invalid character. Please enter the letter.")

    if lives == 0:
        print(hangman_dict[lives])
        print(f"You died! The word was \'{word}\'exit")
    else:
        print(f"Congrats! You guessed the word \'{word}\'")



if __name__ == '__main__':
    play_game()
