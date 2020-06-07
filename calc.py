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
root.geometry("1100x400")

# create a database or connect to one
conn = sqlite3.connect('characters_book.db')

#create cursor
c = conn.cursor()

#create table
'''
c.execute("""CREATE TABLE addresses (
		world text,
		name text,
		lvl integer,
		email text,
		password text
		)""")
'''


#Create submit function for database
def submit():
        
        # have to connect and create cursor in function again.
        conn = sqlite3.connect('characters_book.db')
        c = conn.cursor()

        #Insert into table

        c.execute("INSERT INTO addresses VALUES (:world, :name, :lvl, :email, :password)",
                {
                        'world': world.get(),
                        'name': name.get(),
                        'lvl': lvl.get(),
                        'email': email.get(),
                        'password': password.get()

                })
   
        conn.commit()
        conn.close()

        #clear textboxes
        world.delete(0, END)
        name.delete(0, END)
        lvl.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)
#create query function

def query():
        # have to connect and create cursor in function again.
        conn = sqlite3.connect('characters_book.db')
        c = conn.cursor()

        # Query the database

        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
       # print(records)


        # loop thru results
        print_records = ''

        for record in records:
                print_records += str(record) +" " "\n"
                
        query_label = Label(root, text=print_records)
        query_label.grid(row = 4, column = 0, columnspan =2)

        conn.commit()
        conn.close()

# create textboxes
world = Entry(root, width=30)
world.grid(row=1, column =0)

name = Entry(root, width=30)
name.grid(row=1, column =1)

lvl = Entry(root, width=30)
lvl.grid(row=1, column =2)

email = Entry(root, width=30)
email.grid(row=1, column =3)

password = Entry(root, width=30)
password.grid(row=1, column =4)

#Create text box labels

world_label = Label(root, text ="World", width=30)
world_label.grid(row=0, column = 0)

name_label = Label(root, text ="Name", width=30)
name_label.grid(row=0, column = 1)

lvl_label = Label(root, text ="Lvl", width=30)
lvl_label.grid(row=0, column = 2)

email_label = Label(root, text ="Email", width=30)
email_label.grid(row=0, column = 3)

password_label = Label(root, text ="Password", width=30)
password_label.grid(row=0, column = 4)

#create submit button

submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=2,column = 0, columnspan=5, pady=10, padx=10, ipadx=100)

# Create a query button

query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=3,column = 0, columnspan=5, pady=10, padx=10, ipadx=100)

#commit changes
conn.commit()

#close connection

conn.close()


root.mainloop()








