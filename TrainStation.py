import tkinter as tk

window = tk.Tk()
window.title("Train Station Viewer")

canvas = tk.Canvas(window, height=600, width=800)
canvas.pack()

frm_entry = tk.Frame(master=window)

# frm_entry.grid(row=3, column=3, padx=10)

window.mainloop()
