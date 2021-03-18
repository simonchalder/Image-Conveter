# Imports

from PIL import Image 
from tkinter import Tk, Button, Label, OptionMenu, Entry, StringVar, IntVar, Checkbutton, DISABLED, NORMAL, ACTIVE, W
from tkinter import filedialog


def browseFiles():
    filePath = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("Text files", "*.txt*"),("all files", "*.*")))
    img = Image.open(filePath)
    global outfile
    outfile = img.convert('RGB')

def resizeActive():
    height.config(state=NORMAL)

def resizeDisabled():
    height.config(state=DISABLED)

def checkResize():
    cb = check_var1.get()
    if cb == 1:
        resizeActive()
    else:
        resizeDisabled()

def submit():
    ext = extvar.get()   
    savePath = filedialog.asksaveasfilename(initialdir = "/", title = "Select File", filetypes = (("Text files", "*.txt*"),("all files", "*.*"))) + '.' + ext
    outfile.save(savePath)
    print("file conversion successful")
    quit()

root = Tk()
root.title("Image Converter")
root.geometry('300x230+300+100')

browseButton = Button(root, text="Browse Files", command=browseFiles)
browseButton.grid(column=0, row=0, sticky=W, padx=20, pady=10)

extvar = StringVar(root)
extvar.set('jpeg')

fileTypeLabel = Label(root, text="Choose Required File Format")
fileTypeLabel.grid(column=0, row=1, sticky=W, padx=20, pady=5)

fileType = OptionMenu(root, extvar, "jpeg", "png", "gif")
fileType.grid(column=1, row=1, sticky=W, padx=20, pady=5)

check_var1 = IntVar()
resize = Checkbutton(root, text="Resize Image", variable = check_var1, onvalue=1, offvalue=0, command=checkResize)
resize.grid(column=0, row=2, sticky=W, padx=20, pady=5)

widthLabel = Label(root, text="Width")
widthLabel.grid(column=0, row=3, sticky=W, padx=20, pady=5)

width = Entry(root, width=8, state=DISABLED)
width.insert(0, "Width")
width.grid(column=1, row=3, sticky=W, padx=20, pady=5)

heightLabel = Label(root, text="Height")
heightLabel.grid(column=0, row=4, sticky=W, padx=20, pady=5)

height = Entry(root, width=8, state=DISABLED)
height.insert(0, "Height")
height.grid(column=1, row=4, sticky=W, padx=20, pady=5)

submitButton = Button(root, text="Submit", width=25, command=submit)
submitButton.grid(column=0, row=5, columnspan=2, sticky=W, padx=20, pady=5)

root.mainloop()