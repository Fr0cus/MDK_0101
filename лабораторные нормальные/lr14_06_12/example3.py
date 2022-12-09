from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
python_logo = PhotoImage(file="D:\Code_all\MDK_0101\лабораторные нормальные\lr14_06_12\python.png")
label = ttk.Label(image=python_logo)
label.pack()
root.mainloop()