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





vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient = HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

my_btn = Button(root, text="Click me", command=slide).pack()





root.mainloop()








