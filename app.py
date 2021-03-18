# Imports
from tkinter import *
from PIL import Image 

# #open image in png format 
# img = Image.open(r'C:\Users\user1\Desktop/image1.png') 

# img = img.convert('RGB')

# #The image object is used to save the image in jpg format 

# img.save(r'C:\Users\user1\Desktop/new_image.jpg')

root = Tk()
root.title("Image Converter")

browseButton = Button(root, text="Browse Files")
browseButton.pack()

extvar = StringVar(root)
extvar.set('jpeg')

fileType = OptionMenu(root, extvar, "jpeg", "png", "gif")
fileType.pack()

submitButton = Button(root, text="Submit")
submitButton.pack()

root.mainloop()