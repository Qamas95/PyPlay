from tkinter import *
from tkinter import filedialog
#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('Name of app')




def open():
    root.filename = filedialog.askopenfilename(initialdir="D:/Users/kk/Pulpit/Python/", title="Select A File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    mylabel = Label(root, text=root.filename)


my_btn = Button(root, text="Open file", command=open).pack()

root.mainloop()








