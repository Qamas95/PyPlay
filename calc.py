from tkinter import *
from tkinter import filedialog
import requests
import json
import numpy as np
import matplotlib.pyplot as plt

#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title('Charts')
root.geometry("600x150")


def graph():
    house_prices = np.random.normal(200, 250, 500)
    plt.polar(house_prices)
    plt.show()


my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()

root.mainloop()


