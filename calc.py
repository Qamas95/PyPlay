from tkinter import *

root = Tk()
root.title("Calculator")

entryLabel = Entry(root, width=35, borderwidth=5)
entryLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    #entryLabel.delete(0,END)
    current = entryLabel.get()

    entryLabel.delete(0, END)

    entryLabel.insert(0, str(current) + str(number))

def clear_all():
    entryLabel.delete(0, END)


def button_dodawanie():
    first_number = entryLabel.get()
    global f_num
    global math
    math = "dodawanie"
    f_num = int(first_number)
    entryLabel.delete(0, END)

def button_odejmowanie():
    first_number = entryLabel.get()
    global f_num
    global math
    math = "odejmowanie"
    f_num = int(first_number)
    entryLabel.delete(0, END)


def button_mnozenie():
    first_number = entryLabel.get()
    global f_num
    global math
    math = "mnozenie"
    f_num = int(first_number)
    entryLabel.delete(0, END)

def button_dzielenie():
    first_number = entryLabel.get()
    global f_num
    global math
    math = "dzielenie"
    f_num = int(first_number)
    entryLabel.delete(0, END)

def button_equals():

    second_number = entryLabel.get()
    entryLabel.delete(0, END)


    if math == "dodawanie":
        entryLabel.insert(0, f_num + int(second_number))
    elif math == "odejmowanie":
        entryLabel.insert(0, f_num - int(second_number))
    elif math == "mnozenie":
        entryLabel.insert(0, f_num * int(second_number))
    elif math == "dzielenie":
        entryLabel.insert(0, f_num / int(second_number))

    


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_clear = Button(root, text="Clear", padx=76, pady=20, command=lambda: clear_all())
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_odejmowanie())

button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_mnozenie())
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_dzielenie())
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_dodawanie())

button_equal = Button(root, text="=", padx=86, pady=20, command=lambda: button_equals())


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()








