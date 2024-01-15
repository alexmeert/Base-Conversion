import tkinter as tk
from tkinter import ttk
from conversion_math import *

def tk_window():
    # Create the main window
    root = tk.Tk()
    root.title("Base Conversion Tool")
    root.geometry("550x500")

    # Style configuration (makes the 
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 10), padding=10)
    style.configure("TRadiobutton", font=("Arial", 10), padding=5)

    # Input frame
    input_frame = ttk.Frame(root, padding="10 10 10 10")
    input_frame.pack(fill=tk.BOTH, expand=True)

    # Input label and user-input
    label = ttk.Label(input_frame, text="Enter your integer below:", style="TLabel")
    label.pack()
    user_input = ttk.Entry(input_frame, width=30)
    user_input.pack()

    # Error message label
    error_label = ttk.Label(input_frame, text="", foreground="red", style="TLabel")
    error_label.pack()

    # 'From' base frame
    from_frame = ttk.LabelFrame(input_frame, text="Select the base you are converting from:", padding="10 10 10 10")
    from_frame.pack(fill=tk.BOTH, expand=True)

    from_base = tk.StringVar()
    ttk.Radiobutton(from_frame, text="Decimal", variable=from_base, value="Decimal", style="TRadiobutton").pack(anchor=tk.W)
    ttk.Radiobutton(from_frame, text="Binary", variable=from_base, value="Binary", style="TRadiobutton").pack(anchor=tk.W)
    ttk.Radiobutton(from_frame, text="Octal", variable=from_base, value="Octal", style="TRadiobutton").pack(anchor=tk.W)
    ttk.Radiobutton(from_frame, text="Hex", variable=from_base, value="Hex", style="TRadiobutton").pack(anchor=tk.W)

    # 'To' base frame
    to_frame = ttk.LabelFrame(input_frame, text="Select the base you are converting to:", padding="10 10 10 10")
    to_frame.pack(fill=tk.BOTH, expand=True)

    to_base = tk.StringVar()
    ttk.Radiobutton(to_frame, text="Decimal", variable=to_base, value="Decimal", style="TRadiobutton").pack(anchor=tk.W)
    ttk.Radiobutton(to_frame, text="Binary", variable=to_base, value="Binary", style="TRadiobutton").pack(anchor=tk.W)
    ttk.Radiobutton(to_frame, text="Octal", variable=to_base, value="Octal", style="TRadiobutton").pack(anchor=tk.W)
    ttk.Radiobutton(to_frame, text="Hex", variable=to_base, value="Hex", style="TRadiobutton").pack(anchor=tk.W)

    # Conversion button and result label
    convert_button = ttk.Button(input_frame, text="Convert", command=lambda: convert_number(user_input, from_base, to_base))
    convert_button.pack()
    result_label = ttk.Label(input_frame, text="Result: ", style="TLabel")
    result_label.pack()

    # Function to validate the user's input
    def validate_input():
        error_label.config(text="")  # Clears the error message when the user starts typing
    # Binding the entry widget to clear error message on new input
    user_input.bind("<Key>", lambda event: validate_input())

    def convert_number(entry_widget, from_base, to_base):
        # Clearing previous error message
        error_label.config(text="")

        number = entry_widget.get()
        from_base_val = from_base.get()
        to_base_val = to_base.get()

        try:
            if '.' in number: # Checks if there is a decimal point
                raise ValueError("Floating-point numbers are not supported. Please enter an integer.")

            # Converts from the user-specified base to decimal
            if from_base_val == "Decimal":
                decimal_num = int(number)
            elif from_base_val == "Binary":
                decimal_num = binary_to_decimal(number)
            elif from_base_val == "Octal":
                decimal_num = octal_to_decimal(number)
            elif from_base_val == "Hex":
                decimal_num = hex_to_decimal(number)
            else:
                raise ValueError("Please select a base to convert from")

            # Converts from decimal to the user-entered base
            if to_base_val == "Decimal":
                result = str(decimal_num)
            elif to_base_val == "Binary":
                result = decimal_to_binary(decimal_num)
            elif to_base_val == "Octal":
                result = decimal_to_octal(decimal_num)
            elif to_base_val == "Hex":
                result = decimal_to_hex(decimal_num)
            else:
                raise ValueError("Please select a base to convert to")
        except ValueError as e:
            result = ""
            error_label.config(text=f"Error: {e}")

        result_label.config(text=f"Result: {result}")

    return root

def main():
    tk_window().mainloop() # main function runs the main tkinter gui window function

if __name__ == "__main__":
    main()