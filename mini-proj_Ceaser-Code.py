'''
ШИФР ЦЕЗАРЯ

Описание проекта:
требуется написать программу, способную дешифровать текст в соответствии с алгоритмом Цезаря.
Она должна запрашивать у пользователя следующие данные:
- направление: шифрование или дешифрование;
- язык ялфавита: русский или английский;
- шаг сдвига (со сдвигом вправо)

ПРИМЕЧАНИЯ.
1. В русском языке 32 буквы (буква ё отсутствует)
2. В английском 26 вариаций
2. Неалфавитные сиволы - знаки препинания, пробелы, цифры - не меняются.
3. Сохрание регистр символов.

СОСТАВЛЯЮЩИЕ ПРОЕКТА:
- целые числа(тип int)
- модульная арифметика
- переменные
- ввод и вывод данных
- условный оператор
- цикл
- строковые методы 

ASCII codes:

ENG: 
- capital 65-90
- ref 97-122


'''


'''
1. сделать проверку входящих данных
2. сделать функцию кодирования
3. сделать функцию декодирования
4. проверить, что неалфавитные символы не сдвигаются
5. При этом сохранить регистр

'''


# ________________________________CODING__________________________________________


MAX_ENKEY_SIZE = 26
MAX_RUKEY_SIZE = 32  # we don't count 'ё'


def getLang():
    # we can decrypt/encrypt into two languages
    global current_max

    lang = ''
    current_max = 0
    while True:
        print('Please select a language (en / ru):')
        lang = input()
        if lang not in ('ru', 'en'):
            print('please choose between two variants!')
        elif lang in ('ru', 'en'):
            if lang == 'ru':
                current_max = MAX_RUKEY_SIZE
            else:
                current_max = MAX_ENKEY_SIZE
        break
    return lang


def getKey():
    key = 0
    if lang == 'en':
        while True:
            print('Enter the key number (1-%s)' % (MAX_ENKEY_SIZE))
            key = int(input())
            if (key >= 1 and key <= MAX_ENKEY_SIZE):
                return key
    elif lang == 'ru':
        while True:
            print('Enter the key number (1-%s)' % (MAX_RUKEY_SIZE))
            key = int(input())
            if (key >= 1 and key <= MAX_RUKEY_SIZE):
                return key


def getMode():
    # user can choose: encrypt/decrypt with a key or without it
    while True:
        print('What do you wish to do: encrypt/decrypt or brute force a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode[0]
        else:
            print('Enter either "encrypt"/"e", or "decrypt"/"d", or "brute"/"b".')


def getMessage():
    print('Enter your Message:')
    return input()


def caesarCipherEN(mode, message, key):
    if mode[0] == 'd':  # direction of decryption
        key = -key

    trans_phrase = ''

    for symbol in message:
        num_dec = ord(symbol)

        if symbol.isalpha():
            num_dec = ord(symbol)
            num_dec += key

            if symbol.isupper():
                if num_dec > ord('Z'):
                    num_dec -= current_max
                elif num_dec < ord('A'):
                    num_dec += current_max
            elif symbol.islower():
                if num_dec > ord('z'):
                    num_dec -= current_max
                elif num_dec < ord('a'):
                    num_dec += current_max

            trans_phrase += chr(num_dec)
        else:
            trans_phrase += symbol

    return trans_phrase


def caesarCipherRU(mode, message, key):
    if mode[0] == 'd':  # direction of decryption
        key = -key

    trans_phrase = ''

    for symbol in message:
        num_dec = ord(symbol)

        if symbol.isalpha():
            num_dec += key

            if symbol.isupper():
                if num_dec > ord('Я'):
                    num_dec -= current_max
                elif num_dec < ord('А'):
                    num_dec += current_max
            elif symbol.islower():
                if num_dec > ord('я'):
                    num_dec -= current_max
                elif num_dec < ord('а'):
                    num_dec += current_max

            trans_phrase += chr(num_dec)
        else:
            trans_phrase += symbol

    return trans_phrase


mode, message, lang = getMode(), getMessage(), getLang()
if mode[0] != 'b':
    key = getKey()

print('Your translated test is: ')
if mode[0] != 'b' and lang == 'en':
    print(caesarCipherEN(mode, message, key))
elif mode[0] != 'b' and lang == 'ru':
    print(caesarCipherRU(mode, message, key))
else:
    if lang == 'en':
        for key in range(1, MAX_ENKEY_SIZE + 1):
            print(key, caesarCipherRU(mode, message, key))
    elif lang == 'ru':
        for key in range(1, MAX_RUKEY_SIZE + 1):
            print(key, caesarCipherRU(mode, message, key))

'''
TESTING

1. To be, or not to be, that is the question! (7)
2. Sgd fqzrr hr zkvzr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.(25)
3. Hawnj pk swhg xabkna ukq nqj. (n)
4. Умом Россию не понять.

'''
