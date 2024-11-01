import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("293x468")
        self.root.config(bg="#2E2E2E")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display
        display = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), bg="#FFFFFF", bd=10, insertwidth=4, width=14, borderwidth=4)
        display.grid(row=0, column=0, columnspan=6, sticky='wesn')

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)
    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial Bold", 18), bg="#FFFFFF", command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="wesn")

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("")
        elif char == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
