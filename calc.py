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


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = [
"Mon","Tues","Wed","Thurs","Frid"
]


clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()


myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()








