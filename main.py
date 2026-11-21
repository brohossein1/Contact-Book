import json
import tkinter
from tkinter import messagebox
from tkinter import ttk

contacts = {}
editing_name = None

def save():
    with open("contacts2.json" , "w") as file:
        json.dump(contacts , file)
def load():
    global contacts
    try:
        with open("contacts2.json" , "r") as file:
            contacts = json.load(file)
    except FileNotFoundError :
        contacts = {}
load()

window = tkinter.Tk()
window.title("Contact")
window.geometry("700x500")
window.configure(bg="#2D4059")

button_frame = tkinter.Frame(window , width=700 , height=100)
button_frame.configure(bg="#2D4059")
button_frame.pack(pady=10)

button_frame.pack_propagate(False)

title = tkinter.Label(
    window , 
    text="Contact Hossein" ,
    font=("Arial" , 20),
    bg="#26364A",
    fg="white"
)
title.pack(pady=20)
name_entry = tkinter.Entry(window)
name_entry.pack(pady=5)
number_entry = tkinter.Entry(window)
number_entry.pack(pady=5)

def validate_phone(phone):
    if len(phone) != 11:
        return False
    if not phone.startswith("09"):
        return False
    if not phone.isdigit():
        return False
    return True

def add_contact1():
    namee = name_entry.get()
    numberr = number_entry.get()
    if validate_phone(numberr):
        contacts[namee] = numberr
        save()
        messagebox.showinfo("Success" , "Contact Adedd")

        name_entry.delete(0 , tkinter.END)
        number_entry.delete(0 , tkinter.END)

    else:
        messagebox.showerror("Error" , "Try Again")
    
add_button = tkinter.Button(
    button_frame ,
    text= "Add Contact",
    command = add_contact1
)
add_button.pack(side=tkinter.LEFT , padx=5 , pady=10)


table = ttk.Treeview(
    window ,
    columns = ("name" , "phone") , 
    show = "headings" 
)
table.heading("name" , text="Name")
table.heading("phone" , text="Phone")

def show():
    for item in table.get_children():
        table.delete(item)

    for namee, numberr in contacts.items():
        table.insert("", "end", values=(namee, numberr))

    table.pack(pady=20)
show_button = tkinter.Button(
    button_frame , 
    text="Show Contact" , 
    command = show
)
show_button.pack(side=tkinter.RIGHT, padx=5)

def delete():
    selected = table.selection()

    if not selected:
        messagebox.showerror("Error" , "Select a Contact")
        return

    item = table.item(selected[0])
    namee = item["values"][0]

    contacts.pop(namee)
    save()
    show()
    messagebox.showinfo("Succes2" , "Contact Deleted")

delete_button = tkinter.Button(
    button_frame , 
    text="Delete Contact" , 
    command= delete
)
delete_button.pack(side=tkinter.RIGHT , padx= 5)

def edit():
    global editing_name
    selected = table.selection()

    if not selected:
        messagebox.showerror("Error", "Select a Contact")
        return

    item = table.item(selected[0])
    namee = item["values"][0]
    numberr = item["values"][1]

    editing_name = namee

    name_entry.delete(0, tkinter.END)
    number_entry.delete(0, tkinter.END)

    name_entry.insert(0, namee)
    number_entry.insert(0, numberr)


def update():
    global editing_name

    if editing_name is None:
        messagebox.showerror("Error", "Select a Contact First")
        return

    new_name = name_entry.get()
    new_number = number_entry.get()

    if not validate_phone(new_number):
        messagebox.showerror("Error", "Invalid Phone")
        return

    if new_name in contacts and new_name != editing_name:
        messagebox.showerror("Error", "Name Already Exists")
        return

    contacts.pop(editing_name)
    contacts[new_name] = new_number

    editing_name = None

    save()
    show()

    name_entry.delete(0, tkinter.END)
    number_entry.delete(0, tkinter.END)

    messagebox.showinfo("Success", "Contact Updated")

update_button = tkinter.Button(
    button_frame,
    text="Update Contact",
    command=update
)
update_button.pack(side=tkinter.RIGHT, padx=5)

edit_button = tkinter.Button(
    button_frame , 
    text="Edit Contact",
    command=edit
)
edit_button.pack(side=tkinter.RIGHT, padx=5)

window.mainloop()
