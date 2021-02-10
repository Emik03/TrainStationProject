import tkinter as tk

# Init
window = tk.Tk()
window.title('Train Station Viewer')
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

frm_entry = tk.Frame(master=window)

ent = tk.Entry(master=frm_entry, width=50)
lbl = tk.Label(master=frm_entry, text='Search')

variable = StringVar(master=frm_entry)
variable.set('test')
array = ['test', 'Test', 'Hello', 'World!']
w = tk.OptionMenu(master=frm_entry, variable, *array)
w.pack()

ent.grid(row=0, column=0, sticky='e')
lbl.grid(row=0, column=1, sticky='w')


# Create the conversion Button and result display Label
btn = tk.Button(
    master=window,
    text='Export as JSON',
)

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn.grid(row=0, column=1, pady=10)
lbl.grid(row=0, column=2, padx=10)
lbl.grid(row=1, column=0, padx=10)

# Run the application
window.mainloop()