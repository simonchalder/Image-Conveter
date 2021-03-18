# Imports

from PIL import Image 
from tkinter import Tk, Button, Label, OptionMenu, Entry, StringVar
from tkinter import filedialog

def browseFiles():
    filePath = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("Text files", "*.txt*"),("all files", "*.*")))
    img = Image.open(filePath)
    global outfile
    outfile = img.convert('RGB')
    

def submit():
    ext = extvar.get()   
    savePath = filedialog.asksaveasfilename(initialdir = "/", title = "Select File", filetypes = (("Text files", "*.txt*"),("all files", "*.*"))) + '.' + ext
    outfile.save(savePath)
    print("file conversion successful")
    quit()

root = Tk()
root.title("Image Converter")

browseButton = Button(root, text="Browse Files", command=browseFiles)
browseButton.pack()

extvar = StringVar(root)
extvar.set('jpeg')

fileType = OptionMenu(root, extvar, "jpeg", "png", "gif")
fileType.pack()

submitButton = Button(root, text="Submit", command=submit)
submitButton.pack()

root.mainloop()