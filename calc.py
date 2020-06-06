from tkinter import *

#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title("Frames and stuff")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello")
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clickes yes!").pack()
    else:
        Label(root, text="You clicked no!").pack()


Button(root, text="Popup", command=popup).pack()






root.mainloop()








