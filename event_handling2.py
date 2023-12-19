import tkinter as tk


def concatenate_names():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    full_name = f"{first_name} {last_name}"
    label_result.config(text=f"Concatenated Name: {full_name}")


# Create the main Tkinter window
root = tk.Tk()
root.title("Name Concatenation")

# Create and place widgets in the window
label_first_name = tk.Label(root, text="First Name:")
label_first_name.grid(row=0, column=0, padx=10, pady=10)

entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=10)

label_last_name = tk.Label(root, text="Last Name:")
label_last_name.grid(row=1, column=0, padx=10, pady=10)

entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=10)

button_concatenate = tk.Button(root, text="Concatenate", command=concatenate_names)
button_concatenate.grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Concatenated Name:")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
