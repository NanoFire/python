import tkinter as tk
from math import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Entry widget to display the input and results
        self.entry = tk.Entry(master, font=('Arial', 16), bd=10, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3),
            ('sqrt', 6, 0), ('(', 6, 1), (')', 6, 2), ('C', 6, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, width=4, height=2, font=('Arial', 16), command=lambda t=text: self.click(t))
            button.grid(row=row, column=column)

    def click(self, button):
        current_entry = self.entry.get()

        if button == 'C':
            self.entry.delete(0, tk.END)
        elif button == '=':
            try:
                result = eval(current_entry)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

# Main function to run the calculator
def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    
    main()
