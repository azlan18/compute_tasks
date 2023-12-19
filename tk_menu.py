import tkinter as tk

def on_file_new():
    print("New File")

def on_file_open():
    print("Open File")

def on_file_save():
    print("Save File")

def on_edit_cut():
    print("Cut")

def on_edit_copy():
    print("Copy")

def on_edit_paste():
    print("Paste")

# Create the main Tkinter window
root = tk.Tk()
root.title("Basic Menu Bar")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create file menu and add items
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=on_file_new)
file_menu.add_command(label="Open", command=on_file_open)
file_menu.add_command(label="Save", command=on_file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create edit menu and add items
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=on_edit_cut)
edit_menu.add_command(label="Copy", command=on_edit_copy)
edit_menu.add_command(label="Paste", command=on_edit_paste)

# Start the Tkinter event loop
root.mainloop()
