import tkinter as tk
from tkinter import ttk, font, messagebox
from num_gen import number_generator
from check_string_func import check_string

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Frontend of GUI
        self.title("Number Generator")
        self.geometry("600x300")
        self.iconbitmap("dice_icon.ico")
        self.fontFamilyH1 = font.Font(family = 'Playfair Display', size = 40)
        self.fontFamilyH2 = font.Font(family = 'Playfair Display', size = 25)
        self.fontFamilyH3 = font.Font(family = 'Playfair Display', size = 15)
    
        self.appLabel = ttk.Label(self, text = "Number Generator", font = self.fontFamilyH1)        

        self.mainFrame = ttk.Frame(self)

        # Input fields
        self.inputFrame = ttk.Frame(self.mainFrame)

        self.startValue = tk.StringVar()
        self.startEntry = ttk.Entry(self.inputFrame, textvariable = self.startValue, width = 5, font = self.fontFamilyH2)
        self.startLabel = ttk.Label(self.inputFrame, text = "Start value:", font = self.fontFamilyH2)

        self.endValue = tk.StringVar()
        self.endEntry = ttk.Entry(self.inputFrame, textvariable = self.endValue, width = 5, font = self.fontFamilyH2)
        self.endLabel = ttk.Label(self.inputFrame, text = "End value:", font = self.fontFamilyH2)

        # Generate button
        self.generateButton = tk.Button(self, text = "Generate", font = self.fontFamilyH3, command = self.buttonAction)
        
        # Displays widgets to GUI
        self.appLabel.pack(pady = "5")
        self.mainFrame.pack(pady = "5")
        self.inputFrame.grid()
        self.startLabel.grid(column = 0, row = 0)
        self.startEntry.grid(column = 1, row = 0, padx = 2)
        self.endLabel.grid(column = 0, row = 1)
        self.endEntry.grid(column = 1, row = 1)
        self.generateButton.pack(pady = "15")

    def buttonAction(self):
        if not self.startValue.get() or not self.endValue.get(): # Checks if there are any values in startvalue and endvalue
            messagebox.showerror(title = "No value(s)", message = "Please input value(s) for start value and end value.")
            return
        
        if not check_string(self.startValue.get()) or not check_string(self.endValue.get()): # Checks if start value and end value are integers
            messagebox.showerror(title = "Non-integer value(s)", message = "Start value and end value have to be a number, please try again.")
            return
            
        if int(self.startValue.get()) >= int(self.endValue.get()): # Checks if start value is greater than end value
            messagebox.showerror(title = "Unvalid intervall", message = "End value has to be greater than start value, please try again.")
            return
            
        print("Yay!")

if __name__ == "__main__":
    root = Application()
    root.mainloop()