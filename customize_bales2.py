import tkinter as tk
from tkinter import ttk, colorchooser

def launch_color_selector(var):
    color = colorchooser.askcolor(title="Choose a Color")[1]
    var.set(color)

def update_label():
    label.config(
        text=text_var.get(),
        anchor=anchor_var.get(),
        bg=bg_color_var.get(),
        bd=int(border_width_var.get()),
        relief=border_relief_var.get(),
        width=int(width_var.get()),
        height=int(height_var.get()),
        cursor=cursor_var.get(),
        fg=text_color_var.get()
    )

# Create the main window
root = tk.Tk()
root.title("Label Customization")

# Variables for dropdowns
bg_color_var = tk.StringVar()
border_relief_var = tk.StringVar()
cursor_var = tk.StringVar()
text_color_var = tk.StringVar()

# Default values
bg_color_var.set("white")
border_relief_var.set("solid")
cursor_var.set("arrow")
text_color_var.set("black")

# Create a label
label = tk.Label(root, text="Customize me!", font=('Arial', 12))
label.pack(pady=10)

# Entry for label text
text_var = tk.StringVar()
text_entry = tk.Entry(root, textvariable=text_var, width=30)
text_entry.insert(0, "Updated Text")
text_entry.pack(pady=5)

# Dropdown for text alignment
anchor_var = tk.StringVar()
anchor_dropdown = ttk.Combobox(root, textvariable=anchor_var, values=["w", "e", "center"])
anchor_dropdown.set("w")
anchor_dropdown.pack(pady=5)

# Dropdown for background color
bg_color_dropdown = ttk.Combobox(root, textvariable=bg_color_var, values=["white", "lightblue", "lightgreen"])
bg_color_dropdown.pack(pady=5)

# Dropdown for border relief style
border_relief_dropdown = ttk.Combobox(root, textvariable=border_relief_var, values=["solid", "raised", "sunken"])
border_relief_dropdown.set("solid")
border_relief_dropdown.pack(pady=5)

# Entry for border width
border_width_var = tk.StringVar()
border_width_entry = tk.Entry(root, textvariable=border_width_var, width=10)
border_width_entry.insert(0, "2")
border_width_entry.pack(pady=5)

# Entry for label width
width_var = tk.StringVar()
width_entry = tk.Entry(root, textvariable=width_var, width=10)
width_entry.insert(0, "20")
width_entry.pack(pady=5)

# Entry for label height
height_var = tk.StringVar()
height_entry = tk.Entry(root, textvariable=height_var, width=10)
height_entry.insert(0, "3")
height_entry.pack(pady=5)

# Dropdown for cursor style
cursor_dropdown = ttk.Combobox(root, textvariable=cursor_var, values=["arrow", "hand2", "watch"])
cursor_dropdown.set("arrow")
cursor_dropdown.pack(pady=5)

# Entry for text color
text_color_entry = tk.Entry(root, textvariable=text_color_var, width=10)
text_color_entry.pack(pady=5)

# Button to launch the color selector for text color
text_color_button = tk.Button(root, text="Choose Text Color", command=lambda: launch_color_selector(text_color_var))
text_color_button.pack(pady=5)

# Button to launch the color selector for background color
bg_color_button = tk.Button(root, text="Choose Background Color", command=lambda: launch_color_selector(bg_color_var))
bg_color_button.pack(pady=5)

# Button to update the label
update_button = tk.Button(root, text="Update Label", command=update_label)
update_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
