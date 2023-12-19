import tkinter as tk
from tkinter import messagebox

def on_file_new():
    messagebox.showinfo("New File", "Creating a new file...")

def on_file_open():
    messagebox.showinfo("Open File", "Opening a file...")

def on_file_save():
    messagebox.showinfo("Save File", "Saving the file...")

def on_help_about():
    messagebox.showinfo("About", "This is a simple Tkinter menu example.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Menu Bar Example")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create File menu and add items
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=on_file_new)
file_menu.add_command(label="Open", command=on_file_open)
file_menu.add_command(label="Save", command=on_file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create Help menu and add items
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=on_help_about)

# Start the Tkinter event loop
root.mainloop()
