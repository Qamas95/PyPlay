from tkinter import *

#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('Name of app')



def openWindow():
    top = Toplevel()
    lbl = Label(top, text="Hello").pack()
    btn2 = Button(top, text="Close window", command = top.destroy)
    btn2.pack()

btn = Button(root, text="Open Second Window", command = openWindow)
btn.pack()

root.mainloop()








