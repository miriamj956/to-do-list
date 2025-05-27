from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("To-Do List")

def add_item():
    item = entry1.get()
    if item: 
        list_box.insert(END, item)
        entry1.delete(0, END) 

def delete_item():
    try:
        selected_index = list_box.curselection()[0]
        list_box.delete(selected_index)
    except IndexError:
        pass


label1 = Label(root, text="Make your own to-do list!", font=("Helvetica", 16))
label1.pack(pady=10)

entry1 = Entry(root, width=50)
entry1.pack(pady=5)

button_frame = Frame(root)
button_frame.pack(pady=10)

button1 = Button(button_frame, text="ADD", command=add_item)
button1.grid(row=0, column=0, padx=5)

button2 = Button(button_frame, text="DELETE", command=delete_item)
button2.grid(row=0, column=1, padx=5)

list_frame = Frame(root)
list_frame.pack(pady=10)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

list_box = Listbox(list_frame, width=50, yscrollcommand=scrollbar.set)
list_box.pack()

scrollbar.config(command=list_box.yview)

root.mainloop()
