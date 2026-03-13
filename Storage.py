import tkinter as tk
import time

storage = []

def mdp():
    text = entry.get()
    if text == "1234":
        label.config(text="Access granted")
        
        # wait 1 second then clear the window
        window.after(500, clear_window)
    else:
        label.config(text="Access denied")

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()
    menu()

def menu():
    global result

    button = tk.Button(window, text="view list", command=view_list)
    button.pack(pady=10)

    button = tk.Button(window, text="add item", command=add_item)
    button.pack(pady=10)

    button = tk.Button(window, text="delete item", command=delete_item)
    button.pack(pady=10)

    button = tk.Button(window, text="exit", command=window.destroy)
    button.pack(pady=10)

    result = tk.Label(window, text="")
    result.pack(pady=10)


def add_item():
    add = tk.Entry(window)
    add.pack(pady=10)
    def submit():
        item = add.get()
        storage.append(item)
        result.config(text=f"Item '{item}' added to storage")
        add.destroy()
        submit_button.destroy()
        result.config(text="")
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack(pady=10)


def view_list():
    if storage:
        items = "\n".join(storage)
        result.config(text="Stored items:\n" + items)
    else:
        result.config(text="Storage is empty")


def delete_item():
    delete = tk.Entry(window)
    delete.pack(pady=10)

    def remove():
        item = delete.get()

        if item in storage:
            storage.remove(item)
            result.config(text=f"{item} removed from storage")
            delete.destroy()
            remove_button.destroy()
            result.config(text="")
        else:
            result.config(text="Item not found")

    remove_button = tk.Button(window, text="Delete item", command=remove)
    remove_button.pack(pady=5)


window = tk.Tk()
window.title("storage system")
window.geometry("400x300")

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Submit", command= mdp)
button.pack(pady=10)

# Text display
label = tk.Label(window, text="")
label.pack(pady=10)

# Run the interface
window.mainloop()