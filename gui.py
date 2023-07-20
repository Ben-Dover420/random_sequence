from tkinter import *
from tkinter import ttk
from num_gen import number_generator

class NumberGen:
    def __init__(self, root):
        root.title("Number Generator")


root = Tk()
NumberGen(root)
root.mainloop()