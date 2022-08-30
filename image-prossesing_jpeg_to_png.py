from PIL import Image
import sys
import os

'''
program takes 2params: folder(to take images), new_folder(to put images)

'''


# grab the first and second argument
folder = sys.argv[1]
new_folder = sys.argv[2]

# check if new_folder exists and if not create
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    print(f'new folder "{new_folder}" created')


for filename in os.listdir(folder):
    img = Image.open(f'{folder}{filename}')
    clean_name = os.path.splitext(filename)[0]

    # convert images to png and save to new folder
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print(f'file {filename} converted to {clean_name}.png')
