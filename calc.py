from tkinter import *
from tkinter import filedialog
#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('Name of app')
root.geometry("400x400")

var = StringVar()

c = Checkbutton(root, text="Check this box", variable = var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

def checkcheck():
    test_label = Label(root, text=var.get()).pack()


btn1 = Button(root, text="Click me!", command=checkcheck).pack()




root.mainloop()








