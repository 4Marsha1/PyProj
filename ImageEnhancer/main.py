from PIL import Image,ImageEnhance, ImageFilter
import os

pathIn = './images'
pathOut = './editedImages'

FACTOR = float(input('Enter the factor: '))

for filename in os.listdir(pathIn):
    img = Image.open(f"{pathIn}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(FACTOR)
    enhancer = ImageEnhance.Sharpness(edit)
    edit = enhancer.enhance(FACTOR)
    enhancer = ImageEnhance.Color(edit)
    edit = enhancer.enhance(FACTOR)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f'{pathOut}/{clean_name}_edited.png')