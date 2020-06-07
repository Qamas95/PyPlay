from tkinter import *
from tkinter import filedialog
import sqlite3
#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('Name of app')
root.geometry("400x400")


# create a database or connect to one

conn = sqlite3.connect('characters_book.db')


#create cursor

c = conn.cursor()


#create table

c.execute("""CREATE TABLE addresses (
		world text,
		name text,
		lvl integer,
		email text,
		password text
		)""")


#commit changes
conn.commit()


#close connection

conn.close()


root.mainloop()








