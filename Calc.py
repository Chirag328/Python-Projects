import tkinter as tk

# Function to update the expression on the screen
def click(button_text):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + button_text)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the screen
def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget for displaying the expression
entry = tk.Entry(window, width=25, font=('Arial', 14), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 4)
]

# Create the buttons
for (text, row, col, *span) in buttons:
    button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 14), 
                       command=lambda t=text: click(t) if t != '=' and t != 'C' else evaluate() if t == '=' else clear())
    button.grid(row=row, column=col, columnspan=(span[0] if span else 1), sticky="nsew")

# Make all rows and columns expandable
for r in range(6):
    window.grid_rowconfigure(r, weight=1)
for c in range(4):
    window.grid_columnconfigure(c, weight=1)

# Start the main loop
window.mainloop()
