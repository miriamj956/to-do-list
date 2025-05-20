from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("To-Do List")

def idk():
    get1 = entry1.get()
    list.config(text=get1)


label1 = Label(root, text="Make your own to do list!")
label1.pack()

entry1 = Entry(root)
entry1.pack()

button1 = Button(root, text="ADD", command=idk)
button1.pack()

list = Label(root, text= " ")
list.pack()




root.mainloop()