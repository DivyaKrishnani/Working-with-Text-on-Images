

from pytesseract import image_to_string
from PIL import Image

im = Image.open('images/img1.jpeg')
print(im)

print(image_to_string(im))  
#fw = open("out1.txt" , "w")
#fw.write(image_to_string(im))


