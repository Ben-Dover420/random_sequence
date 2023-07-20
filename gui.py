import tkinter as tk
from tkinter import ttk
from num_gen import number_generator

class NumberGen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Generator")
        self.geometry("900x500")
        self.iconbitmap("dice_icon.ico")

if __name__ == "__main__":
    root = NumberGen()
    root.mainloop()