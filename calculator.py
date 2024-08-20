import tkinter as tk

class AdvancedCalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Advanced Calculator")
        self.calculation_history = []

        # Entry fields for numbers
        self.first_number_entry = tk.Entry(window, width=20)
        self.first_number_entry.grid(row=0, column=0, padx=10, pady=10)

        self.second_number_entry = tk.Entry(window, width=20)
        self.second_number_entry.grid(row=1, column=0, padx=10, pady=10)

        # Dropdown menu for selecting operation
        self.operation_var = tk.StringVar(window)
        self.operation_var.set("+")  # Default operation
        self.operation_menu = tk.OptionMenu(window, self.operation_var, "+", "-", "*", "/", "%", "^")
        self.operation_menu.grid(row=0, column=1, padx=10, pady=10)

        # Button to perform the calculation
        self.calculate_button = tk.Button(window, text="Calculate", command=self.perform_calculation)
        self.calculate_button.grid(row=1, column=1, padx=10, pady=10)

        # Button to clear the input and result
        self.clear_button = tk.Button(window, text="Clear", command=self.clear_entries)
        self.clear_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Label to display the result
        self.result_label = tk.Label(window, text="Result will appear here", font=('Arial', 12))
        self.result_label.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # History label
        self.history_label = tk.Label(window, text="History:", font=('Arial', 10))
        self.history_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Listbox to display calculation history
        self.history_listbox = tk.Listbox(window, width=50, height=10)
        self.history_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def perform_calculation(self):
        try:
            num1 = float(self.first_number_entry.get())
            num2 = float(self.second_number_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            elif operation == "%":
                result = num1 % num2
            elif operation == "^":
                result = num1 ** num2
            else:
                result = "Error: Invalid operation"

            if isinstance(result, float) or isinstance(result, int):
                result_str = f"{num1} {operation} {num2} = {result}"
                self.calculation_history.append(result_str)
                self.history_listbox.insert(tk.END, result_str)

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Error: Please enter valid numbers")

    def clear_entries(self):
        self.first_number_entry.delete(0, tk.END)
        self.second_number_entry.delete(0, tk.END)
        self.result_label.config(text="Result will appear here")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()
