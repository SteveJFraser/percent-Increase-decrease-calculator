import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font

root = tk.Tk()
root.geometry("620x150")
root.resizable(False, False)
root.title("percent increase/Decrease calculator".title())

font.nametofont("TkDefaultFont").configure(size=10)

frame = ttk.Frame(root)
frame.grid(column=3, row=0)
main = ttk.Frame(root)
main.grid(column=0, row=0)

new_value = tk.StringVar()
old_value = tk.StringVar()
increase_value = tk.StringVar()

cows_sheep = Image.open("Percent-increase-decrease-calculator-main\image.jpg").resize((260, 147))
photo = ImageTk. PhotoImage(cows_sheep)


def calc_increase(*args):
    try:
        old = float(old_value.get())
        new = float(new_value.get())
        increase = ((new-old)/old*100)
        increase_value.set(f"{increase:.2f} %")
    except ValueError:
        increase_value.set("try again")


out_put = ttk.Label(main,textvariable=increase_value)
out_put.grid(column=1, row=3, sticky="W")
image_label = ttk.Label(frame, image=photo)
image_label.grid(column=3, row=0)
stock_increase = ttk.Label(main, text="Increase/Decrease: ")
stock_increase.grid(column=0, row=3)
label_1 = ttk.Label(main, text="Base Stock: ")
label_1.grid(column=0, row=0, padx=5, pady=5)
label_2 = ttk.Label(main, text="Total Stock: ")
label_2.grid(column=0, row=1)

entry_1 = ttk.Entry(main, width=15, textvariable=old_value)
entry_1.grid(column=1, row=0)
entry_2 = ttk.Entry(main, width=15, textvariable=new_value)
entry_2.grid(column=1, row=1)

button_1 = ttk.Button(main, text="Calculate", command=calc_increase)
button_1.grid(column=2, row=1)
quit_button = ttk.Button(main, text="Quit", command=root.destroy)
quit_button.grid(column=2, row=0)

for child in main.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.bind("<Return>", calc_increase)
root.bind("<KP_Enter>", calc_increase)

root.mainloop()
