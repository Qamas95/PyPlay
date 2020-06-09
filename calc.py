from tkinter import *
from tkinter import filedialog
import sqlite3
#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

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

#create edit function to update a 

def update():

        record_id = delete_box.get()

        conn = sqlite3.connect('characters_book.db')
        c = conn.cursor()

        record_id = delete_box.get()

        c.execute("""UPDATE addresses SET
        world = :world,
        name = :name,
        lvl = :lvl,
        email = :email,
        password = :password

        WHERE oid = :oid""",
        {
        'world': world_editor.get(),
        'name': name_editor.get(),
        'lvl': lvl_editor.get(),
        'email': email_editor.get(),
        'password': password_editor.get(),
        'oid' : record_id
        })


        conn.commit()
        conn.close()
        editor.destroy()
        root.deiconify()


        
def edit():

        root.withdraw()
        global editor
        if delete_box.get() == '':
                return messagebox.showerror('Warning','Empty ID number')
                editor.destroy()
                root.deiconify()

        editor = Tk()
        editor.title('Editor UI')
        editor.geometry("1100x400")


        conn = sqlite3.connect('characters_book.db')
        c = conn.cursor()

        # Query the database

        record_id = delete_box.get()

        c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        records = c.fetchall()


        global world_editor
        global name_editor
        global lvl_editor
        global email_editor
        global password_editor

        # create textboxes
        world_editor = Entry(editor, width=30)
        world_editor.grid(row=1, column =0)

        name_editor = Entry(editor, width=30)
        name_editor.grid(row=1, column =1)

        lvl_editor = Entry(editor, width=30)
        lvl_editor.grid(row=1, column =2)

        email_editor = Entry(editor, width=30)
        email_editor.grid(row=1, column =3)

        password_editor = Entry(editor, width=30)
        password_editor.grid(row=1, column =4)



        #Create text box labels

        world_label = Label(editor, text ="World", width=30)
        world_label.grid(row=0, column = 0)

        name_label = Label(editor, text ="Name", width=30)
        name_label.grid(row=0, column = 1)

        lvl_label = Label(editor, text ="Lvl", width=30)
        lvl_label.grid(row=0, column = 2)

        email_label = Label(editor, text ="Email", width=30)
        email_label.grid(row=0, column = 3)

        password_label = Label(editor, text ="Password", width=30)
        password_label.grid(row=0, column = 4)

        #loop thru results

        for record in records:
                world_editor.insert(0, record[0])
                name_editor.insert(0, record[1])
                lvl_editor.insert(0, record[2])
                email_editor.insert(0, record[3])
                password_editor.insert(0, record[4])

        # create save button to save edited record
        edit_btn = Button(editor, text="Save Record", command=update)
        edit_btn.grid(row=2,column = 0, columnspan=5, pady=10, padx=10, ipadx=100)



# Create functioon to delete a record

def delete():
        conn = sqlite3.connect('characters_book.db')
        c = conn.cursor()



        if delete_box.get() is '':
                return messagebox.showwarning('Warning', 'Empty Select ID field!')
                
    
        c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
        #Delete a record
        #c.execute("DELETE from addresses WHERE oid = " + delete_box.get())



        conn.commit()
        conn.close()

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
        query_label.grid(row = 7, column = 0, columnspan =5)

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


#create delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=5,column = 0, columnspan=5, pady=10, padx=10, ipadx=100)


delete_box = Entry(root, width=30)
delete_box.grid(row=4, column=0, columnspan=5)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=4, column=1, columnspan=5)


# create an update button

edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=6,column = 0, columnspan=5, pady=10, padx=10, ipadx=100)


#commit changes
conn.commit()

#close connection

conn.close()


root.mainloop()


