import tkinter as tk
import customtkinter as ct # type: ignore
from functions import randSeq # type: ignore
from tkinter import messagebox
from check_string_func import check_string # type: ignore
import pyglet # type: ignore
from PIL import Image

ct.set_appearance_mode("System")
ct.set_default_color_theme("dark-blue")
pyglet.font.add_file('Roboto-Regular.ttf')

class Application(ct.CTk):
    def __init__(self):
        super().__init__()

        # Frontend of GUI
        self.title("Random Sequence Generator")
        self.geometry("600x330")
        self.iconbitmap("dice.ico")
        self.resizable(width = False, height = False)

        fontFamilyH1 = ('Roboto Normal', 60) 
        fontFamilyH2 = ('Roboto Normal', 40)
        fontFamilyH3 = ('Roboto Normal', 20)
        widthEntry = 150

        appLabel = ct.CTkLabel(self, text = "Random Sequences", font = fontFamilyH1)

        # Information button
        infoImage = ct.CTkImage(light_image = Image.open("information-button.png"), dark_image = Image.open("information-button - dark.png"), size = (25, 25))
        infoButton = ct.CTkButton(self, image = infoImage, text = "", command = self.infoButton, fg_color = "transparent", hover_color = ("#f3f2f2", "#202020"), width = 0, height = 0)
        
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
        infoButton.pack(anchor = "e", pady = 5)
        appLabel.pack()    
        inputFrame.pack(pady = 15)
        startLabel.grid(column = 0, row = 0)
        startEntry.grid(column = 1, row = 0, padx = 2)
        endLabel.grid(column = 0, row = 1)
        endEntry.grid(column = 1, row = 1)
        generateButton.pack(pady = "25")

    def buttonAction(self):
        # Conditions before using randSeq function.
        if not self.startValue.get() or not self.endValue.get(): # Checks if there are any values in startvalue and endvalue
            messagebox.showerror(title = "No value(s)", message = "Please input value(s) for start value and end value.")
            return

        if not ((self.startValue.get().isnumeric() and self.endValue.get().isnumeric()) or (self.startValue.get().isalpha() and self.endValue.get().isalpha())): # Checks if we have numbers values
            messagebox.showerror(title = "Incorrect values", message = "The start- and/or end values appear to be neither a number nor a letter. Please input the correct values. If you want to input your own values, do so in Advanced settings.")    
            return
        #not (self.startValue.get().isalpha() and self.endValue.get().isalpha()) 
        randNumLet = randSeq(self.startValue.get(), self.endValue.get()) # Initiates when every condition is met
        
        randList = "" # The randomised list

        for i, elem in enumerate(randNumLet):
             randList += f"Item ({i}): {elem}\n"

        messagebox.showinfo(title = "Randomised list", message = randList)
    
    def infoButton(self):
            messagebox.showinfo(title = "How to use the program", message = "Welcome to Random Sequence Generator! In this program, you can generate elements in a sequence in a random order. You can, by default, generate a random sequence of numbers and letters by entering your desired order in Start value and End value. If you want to skip certain elements, generate random elements from a unique list, or change the appearence of the program, then go to Advanced settings. Have fun!")
            return

if __name__ == "__main__":
    root = Application()
    root.mainloop()