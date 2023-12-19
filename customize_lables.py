import tkinter as tk
from tkinter import ttk, colorchooser

def launch_color_selector():
    color = colorchooser.askcolor(title="Choose a Color")[1]
    label.config(fg=color)

def update_font():
    selected_font = font_var.get()
    selected_style = style_var.get()
    
    font = (selected_font, 12, selected_style)
    label.config(font=font)

# Create the main window
root = tk.Tk()
root.title("Label and Button Customization")

# Create a label
label = tk.Label(root, text="Customize me!", font=('Arial', 12))
label.pack(pady=10)

# Create a button to launch the color selector
color_button = tk.Button(root, text="Choose Color", command=launch_color_selector)
color_button.pack(pady=5)

# Create a dropdown for font family
font_options = ['Arial', 'Times New Roman', 'Courier New']
font_var = tk.StringVar()
font_dropdown = ttk.Combobox(root, textvariable=font_var, values=font_options, state="readonly")
font_dropdown.set('Arial')
font_dropdown.pack(pady=5)

# Create a dropdown for font style
style_options = ['normal', 'bold', 'italic', 'bold italic']
style_var = tk.StringVar()
style_dropdown = ttk.Combobox(root, textvariable=style_var, values=style_options, state="readonly")
style_dropdown.set('normal')
style_dropdown.pack(pady=5)

# Button to update the font
update_font_button = tk.Button(root, text="Update Font", command=update_font)
update_font_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
