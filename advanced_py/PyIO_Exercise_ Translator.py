from fnmatch import translate
from ftplib import error_reply
from translate import Translator  # need to install pip install translate

translator = Translator(to_lang='ja')

try:
    with open('./test.txt', mode='r+w') as file:
        text = file.read()
        translated = Translator(text)
        with open('./test-ja.txt', mode='w') as ja_file:
            ja_file.write(translated)
            print('your translated file is ready!')
except FileNotFoundError:
    print('not existing file')
except IOError as err:
    print('can\'t read this file')
    raise err
