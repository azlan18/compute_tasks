import tkinter as tk

def on_button_click(action):
    label.config(text=f"Button '{action}' Clicked!")

# Create the main window
window = tk.Tk()
window.title("Button Click Event Handling")

# Create buttons with different actions
button1 = tk.Button(window, text="Action 1", command=lambda: on_button_click("Action 1"))
button2 = tk.Button(window, text="Action 2", command=lambda: on_button_click("Action 2"))
button3 = tk.Button(window, text="Action 3", command=lambda: on_button_click("Action 3"))

# Create a label to display the message
label = tk.Label(window, text="Waiting for button click...")

# Pack buttons and label
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
label.pack()

# Run the Tkinter event loop
window.mainloop()
