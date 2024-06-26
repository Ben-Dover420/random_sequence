import tkinter as tk
import customtkinter as ct
from tkinter import ttk, font, messagebox
from num_gen import number_generator
from check_string_func import check_string

"""
class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Frontend of GUI
        self.title("Number Generator")
        self.geometry("600x280")
        self.iconbitmap("dice.ico")

        fontFamilyH1 = font.Font(size = 40)
        fontFamilyH2 = font.Font(size = 25)

        appLabel = ttk.Label(self, text = "Number Generator", font = fontFamilyH1)        

        # Input fields
        inputFrame = ttk.Frame(self)

        self.startValue = tk.StringVar()
        startEntry = ttk.Entry(inputFrame, textvariable = self.startValue, width = 5, font = fontFamilyH2)
        startLabel = ttk.Label(inputFrame, text = "Start value:", font = fontFamilyH2)

        self.endValue = tk.StringVar()
        endEntry = ttk.Entry(inputFrame, textvariable = self.endValue, width = 5, font = fontFamilyH2)
        endLabel = ttk.Label(inputFrame, text = "End value:", font = fontFamilyH2)

        # Generate button
        generateButton = ttk.Button(self, text = "Generate", width = 15, command = self.buttonAction) 
        
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
            
        numbers = number_generator(int(self.startValue.get()), int(self.endValue.get())) # Initiates when every condition is met
        
        for number in range(len(numbers)):
            messagebox.showinfo(title = "Random numbers", message = f"Random number ({number + 1}): {numbers[number]}")

if __name__ == "__main__":
    root = Application()
    root.mainloop()"""

# UI
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

root = ct.CTk()
root.geometry("600x280")
root.title("Number Generator")
root.iconbitmap("dice.ico")

appLabel = ct.CTkLabel(root, text = "Number Generator")  
appLabel.pack()  

if __name__ == "__main__":
    root.mainloop()