import tkinter as tk
from time import strftime

def update_time(label_input):
    current_time = strftime('%H:%M:%S %p')
    label_input.config(text=current_time)
    label_input.after(1000, update_time, label_input)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label for displaying the time
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')

# Run the update_time function to initialize the time display
update_time(time_label)

# Run the Tkinter event loop
root.mainloop()
