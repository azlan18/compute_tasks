import tkinter as tk
from tkinter import colorchooser, filedialog
import os

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        window.configure(bg=color)

def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    if file_path and (file_path.lower().endswith(('.png', '.jpeg', '.jpg'))):
        original_image = tk.PhotoImage(file=file_path)
        resized_image = original_image.subsample(5, 5)

        image_label.configure(image=resized_image)
        image_label.image = resized_image  # To prevent garbage collection

# Main function



window = tk.Tk()
window.title("Color and Image Chooser")

# Button to choose color
color_button = tk.Button(window, text="Choose Color", command=choose_color)
color_button.pack()

# Button to choose image
image_button = tk.Button(window, text="Choose Image", command=choose_image)
image_button.pack()

# Label to display the chosen image
image_label = tk.Label(window, text="Chosen Image:")
image_label.pack()

window.mainloop()

