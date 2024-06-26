import tkinter as tk
import customtkinter as ct
from functions import randSeq
from tkinter import ttk, messagebox
from check_string_func import check_string
import pyglet

ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")
pyglet.font.add_file('Roboto-Regular.ttf')

class Application(ct.CTk):
    def __init__(self):
        super().__init__()

        # Frontend of GUI
        self.title("Random Sequence Generator")
        self.geometry("600x280")
        self.iconbitmap("dice.ico")

        fontFamilyH1 = ('Roboto Normal', 60) 
        fontFamilyH2 = ('Roboto Normal', 40)
        fontFamilyH3 = ('Roboto Normal', 20)
        widthEntry = 150

        appLabel = ct.CTkLabel(self, text = "Random Sequences", font = fontFamilyH1) 
        appLabel.pack(pady = "15")       
        
        # Input fields
        inputFrame = ct.CTkFrame(self)

        self.startValue = tk.StringVar()
        startEntry = ct.CTkEntry(inputFrame, textvariable = self.startValue, width = widthEntry, font = fontFamilyH2)
        startLabel = ct.CTkLabel(inputFrame, text = "Start value:", font = fontFamilyH2)

        self.endValue = tk.StringVar()
        endEntry = ct.CTkEntry(inputFrame, textvariable = self.endValue, width = widthEntry, font = fontFamilyH2)
        endLabel = ct.CTkLabel(inputFrame, text = "End value:", font = fontFamilyH2)

        # Generate button
        generateButton = ct.CTkButton(self, text = "Generate", font = fontFamilyH3, command = self.buttonAction, width = 200, height = 200) 
        
        # Displays widgets to GUI
        appLabel.pack(pady = "15")    
        inputFrame.pack()
        startLabel.grid(column = 0, row = 0)
        startEntry.grid(column = 1, row = 0, padx = 2)
        endLabel.grid(column = 0, row = 1)
        endEntry.grid(column = 1, row = 1)
        generateButton.pack(pady = "25")

    def buttonAction(self):
        if not self.startValue.get() or not self.endValue.get(): # Checks if there are any values in startvalue and endvalue
            messagebox.showerror(title = "No value(s)", message = "Please input value(s) for start value and end value.")
            return
        
        if not check_string(self.startValue.get()) or not check_string(self.endValue.get()): # Checks if start value and end value are integers
            messagebox.showerror(title = "Non-integer value(s)", message = "Start value and end value have to be a number, please try again.")
            return
            
        if int(self.startValue.get()) >= int(self.endValue.get()): # Checks if start value is greater than end value
            messagebox.showerror(title = "Invalid intervall", message = "End value has to be greater than start value, please try again.")
            return
            
        numbers = randSeq(int(self.startValue.get()), int(self.endValue.get())) # Initiates when every condition is met
        
        for number in range(len(numbers)):
            messagebox.showinfo(title = "Random numbers", message = f"Random number ({number + 1}): {numbers[number]}")

if __name__ == "__main__":
    root = Application()
    root.mainloop()