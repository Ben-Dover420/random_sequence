import tkinter as tk
from tkinter import ttk
from num_gen import number_generator

class NumberGen(tk.Tk):
    def __init__(self):
        self.title("Number Generator")
        self.geometry("520x300")
        self.iconbitmap("dice_icon.png")

if __name__ == "__main__":
    root = NumberGen()
    root.mainloop()