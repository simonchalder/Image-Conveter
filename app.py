# Imports

from PIL import Image 

#open image in png format 
img = Image.open(r'C:\Users\user1\Desktop/image1.png') 

img = img.convert('RGB')

#The image object is used to save the image in jpg format 

img.save(r'C:\Users\user1\Desktop/new_image.jpg')