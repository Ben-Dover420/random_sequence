import tkinter as tk
from tkinter import ttk
from num_gen import number_generator

font_family = "Georgia"
h1 = 25
h2 = 15
p = 10
bg_color = "#008080"


class NumberGen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Generator")
        self.geometry("300x170")
        self.resizable(False, False)
        self.iconbitmap("dice_icon.ico")

        self.appLabel = ttk.Label(self, text = "Number Generator", font = (font_family, h1))        

        self.mainFrame = ttk.Frame(self)

        # Input fields
        self.inputFrame = ttk.Frame(self.mainFrame)

        self.startValue = tk.StringVar()
        self.startEntry = ttk.Entry(self.inputFrame, textvariable = self.startValue, font = (font_family, h2), width = 5)
        self.startLabel = ttk.Label(self.inputFrame, text = "Start value:", font = (font_family, h2))

        self.endValue = tk.StringVar()
        self.endEntry = ttk.Entry(self.inputFrame, textvariable = self.endValue, font = (font_family, h2), width = 5)
        self.endLabel = ttk.Label(self.inputFrame, text = "End value:", font = (font_family, h2))

        # Generate button
        self.generateButton = ttk.Button(self.mainFrame, text = "Generate")

        self.appLabel.pack(pady = "5")
        self.mainFrame.pack(pady = "5")
        self.inputFrame.grid()
        self.startLabel.grid(column = 0, row = 0)
        self.startEntry.grid(column = 1, row = 0)
        self.endLabel.grid(column = 0, row = 1)
        self.endEntry.grid(column = 1, row = 1)
        self.generateButton.grid(pady = "10")

if __name__ == "__main__":
    root = NumberGen()
    root.mainloop()