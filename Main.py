import tkinter as tk
from math import *

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')

# Function to update the entry
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to delete last character
def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

# Memory functions
memory = 0
def memory_store():
    global memory
    try:
        memory = eval(entry.get())
    except Exception:
        memory = 0

def memory_recall():
    entry.insert(tk.END, str(memory))

def memory_clear():
    global memory
    memory = 0

# Handle keyboard input
def key_press(event):
    key = event.keysym
    if key in '0123456789+-*/().':
        button_click(event.char)
    elif key == 'Return':
        evaluate_expression()
    elif key == 'BackSpace':
        backspace()
    elif key == 'Escape':
        clear()
    elif key == 'Left':
        entry.icursor(entry.index(tk.INSERT) - 1)
    elif key == 'Right':
        entry.icursor(entry.index(tk.INSERT) + 1)
    elif key.lower() in ['s', 'c', 't', 'p', 'l']:  # Handle scientific functions
        functions = {'s': 'sin(', 'c': 'cos(', 't': 'tan(', 'p': 'pow(', 'l': 'log('}
        button_click(functions[key.lower()])
    elif key == 'm':
        memory_store()
    elif key == 'r':
        memory_recall()
    elif key == 'x':
        memory_clear()

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")

# Configure grid to be responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Frame for entry and buttons
frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Configure frame grid
for i in range(7):
    frame.rowconfigure(i, weight=1)
for j in range(5):
    frame.columnconfigure(j, weight=1)

# Entry widget
entry = tk.Entry(frame, width=40, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('←', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), (')', 4, 3), ('=', 4, 4),
    ('sqrt', 5, 0), ('pow', 5, 1), ('log', 5, 2), ('sin', 5, 3), ('cos', 5, 4),
    ('tan', 6, 0), ('M+', 6, 1), ('M-', 6, 2), ('MR', 6, 3), ('MC', 6, 4)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(frame, text=text, width=10, height=2, font=('Arial', 14), command=evaluate_expression).grid(row=row, column=col, sticky="nsew")
    elif text == 'C':
        tk.Button(frame, text=text, width=10, height=2, font=('Arial', 14), command=clear).grid(row=row, column=col, sticky="nsew")
    elif text == '←':
        tk.Button(frame, text=text, width=10, height=2, font=('Arial', 14), command=backspace).grid(row=row, column=col, sticky="nsew")
    elif text == 'M+':
        tk.Button(frame, text=text, width=10, height=2, font=('Arial', 14), command=memory_store).grid(row=row, column=col, sticky="nsew")
    elif text == 'M-':
        tk.Button(frame, text=text, width=10, height=2, font=('Arial', 14), command=memory_clear).grid(row=row, column=col, sticky="nsew")
    elif text == 'MR':
        tk.Button(frame, text=text, width=10, height=2, font=('Arial', 14), command=memory_recall).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(frame, text=text, width=10, height=2, font=('Arial', 14), command=lambda value=text: button_click(value)).grid(row=row, column=col, sticky="nsew")

# Bind keyboard input
root.bind('<Key>', key_press)

# Make the main window responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Run the application
root.mainloop()
