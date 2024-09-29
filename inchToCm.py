import tkinter as tk

def inch_to_cm(inch):

    cm=inch*2.54

# Set-up the window
window = tk.Tk()
window.title("inch to cm Converter")
window.resizable(width=False, height=False)


# widget and label in it
frm_entry = tk.Frame(master=window)
ent_inches = tk.Entry(master=frm_entry, width=10)
lbl_inch = tk.Label(master=frm_entry, text="\N{Inches_to_cm}")

# using the .grid() geometry manager
ent_inches.grid(row=0, column=0, sticky="e")
lbl_inch.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="-->",
    command=inch_to_cm
)
lbl_result = tk.Label(master=window, text="\N{cm}")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()