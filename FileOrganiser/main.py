import os 
import shutil

PATH = '/Users/abhishek/Desktop'

list_of_files = os.listdir(PATH)

for file in list_of_files:
    if os.path.isdir(f"{PATH}/{file}"):
        continue
    name, extension = os.path.splitext(file)
    extension = extension[1:]
    print(name, extension)

    if os.path.exists(f"{PATH}/{extension}"):
        shutil.move(f"{PATH}/{file}", f"{PATH}/{extension}/{file}")
    else: 
        os.makedirs(f"{PATH}/{extension}")
        shutil.move(f"{PATH}/{file}", f"{PATH}/{extension}/{file}")
