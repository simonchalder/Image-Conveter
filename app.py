# Imports

from PIL import Image 
from tkinter import Tk, Button, Label, OptionMenu, Entry, StringVar, IntVar, Checkbutton, DISABLED, NORMAL, ACTIVE, W
from tkinter import filedialog

# Function Definitions --------------------------------------------------------------------------------------------------------------------------------

def browseFiles(): # Function called when 'Browse Files' button clicked
    filePath = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("Text files", "*.txt*"),("all files", "*.*"))) # Filepath open, assign to variable
    img = Image.open(filePath) # Open image file
    global outfile # create global variable to store image object so it can be used in functions
    outfile = img.convert('RGB') # Conversion to RGB necessary for other file formats

def resizeActive(): # Function to change state of entry boxes
    height.config(state=NORMAL)
    width.config(state=NORMAL)

def resizeDisabled():  # Function to change state of entry boxes
    height.config(state=DISABLED)
    width.config(state=NORMAL)

def checkResize(): # Function called when checkbutton is clicked
    cb = check_var1.get()
    if cb == 1:
        resizeActive()
    else:
        resizeDisabled()

def submit(): # Function called when submit button is clicked
    width_out = width.get()
    height_out = height.get()

    # Logic to determine if file needs to be resized or not

    if check_var1.get() == 1 and width_out != '' and height_out != '':
        size = (int(width_out), int(height_out)) # size is tuple of values for width and height inputs
        ext = extvar.get() # get file extension for conversion  
        savePath = filedialog.asksaveasfilename(initialdir = "/", title = "Select File", filetypes = (("Text files", "*.txt*"),("all files", "*.*"))) + '.' + ext
        outfile.thumbnail(size) # set size dimensions for file save
        outfile.save(savePath) # save new file
        print("file conversion successful")
        quit()
    else:   
        ext = extvar.get()   
        savePath = filedialog.asksaveasfilename(initialdir = "/", title = "Select File", filetypes = (("Text files", "*.txt*"),("all files", "*.*"))) + '.' + ext
        outfile.save(savePath)
        print("file conversion successful")
        quit()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tkinter App & Widgets ---------------------------------------------------------------------------------------------------------------------------------------

root = Tk() # Create root object
root.title("Image Converter")
root.geometry('300x230+300+100') # Window size and starting position

# Widgets

browseButton = Button(root, text="Browse Files", command=browseFiles)
browseButton.grid(column=0, row=0, sticky=W, padx=20, pady=10)

fileTypeLabel = Label(root, text="Choose Required File Format")
fileTypeLabel.grid(column=0, row=1, sticky=W, padx=20, pady=5)

extvar = StringVar(root)
extvar.set('jpeg')

fileType = OptionMenu(root, extvar, "jpeg", "png", "gif", "bmp", "tiff") # file formats are read from their extensions
fileType.grid(column=1, row=1, sticky=W, padx=20, pady=5)

check_var1 = IntVar()
resize = Checkbutton(root, text="Resize Image", variable = check_var1, onvalue=1, offvalue=0, command=checkResize)
resize.grid(column=0, row=2, sticky=W, padx=20, pady=5)

widthLabel = Label(root, text="Width")
widthLabel.grid(column=0, row=3, sticky=W, padx=20, pady=5)

width = Entry(root, width=8, state=DISABLED) # Width and height boxes are disabled until resize box is ticked
width.grid(column=1, row=3, sticky=W, padx=20, pady=5)

heightLabel = Label(root, text="Height")
heightLabel.grid(column=0, row=4, sticky=W, padx=20, pady=5)

height = Entry(root, width=8, state=DISABLED)
height.grid(column=1, row=4, sticky=W, padx=20, pady=5)

submitButton = Button(root, text="Submit", width=25, command=submit)
submitButton.grid(column=0, row=5, columnspan=2, sticky=W, padx=20, pady=5)

root.mainloop()