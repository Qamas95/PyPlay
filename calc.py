from tkinter import *

#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Frames and stuff")

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)


b = Button(frame, text="Test button")
b2 = Button(frame, text="Test2 button")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()








