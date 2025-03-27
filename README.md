# Scientific-Calculator
Welcome to the Scientific Calculator application! This Python-based application allows you to perform basic arithmetic operations along with advanced scientific functions. Built with Tkinter, the app provides an intuitive graphical user interface that supports keyboard input, memory functions, and error handling.

✨ Features
✅ Basic Arithmetic Operations: Addition, subtraction, multiplication, and division.
✅ Scientific Functions: Supports square root, power, logarithms, and trigonometric functions (sin, cos, tan).
✅ Memory Functions:

M+ – Store a value in memory.

MR – Recall the value from memory.

MC – Clear memory.

✅ Error Handling: Displays an error message if an invalid expression is entered.
✅ Keyboard Shortcuts: Perform calculations quickly using your keyboard.
✅ Responsive Interface: Buttons and entry field adapt dynamically to different window sizes.

🛠️ Requirements
Python 3.x: The application is developed using Python 3.

Tkinter: GUI built with the Tkinter library, included by default in most Python installations.

Math Library: Supports advanced mathematical operations like sin(), cos(), tan(), sqrt(), etc.

📥 Installation
Install Python:
Download and install Python from python.org.

No Additional Libraries Required:
Tkinter comes pre-installed with Python, so you don’t need to install any external packages.

🚀 How to Run the Application
Download or Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-repo/scientific-calculator.git
cd scientific-calculator
Run the Script:

bash
Copy
Edit
python calculator.py
The calculator window will open, ready for use.

🎮 How to Use
Basic Operations: Use the numeric and operator buttons to perform calculations.

Scientific Functions: Click or type the function name (e.g., sin, cos, tan, log).

Memory Functions:

M+: Store the current value.

MR: Recall the stored value.

MC: Clear the stored value.

Keyboard Shortcuts:

Enter – Evaluate the expression.

Backspace – Delete the last character.

Esc – Clear the entry.

s, c, t, p, l – Shortcut for sin(), cos(), tan(), pow(), and log() respectively.

📚 Code Overview
Main Functions:
evaluate_expression(): Evaluates the expression entered in the input field.

button_click(value): Adds the specified value to the entry field.

clear(): Clears the input field.

backspace(): Deletes the last character.

memory_store(), memory_recall(), memory_clear(): Manages memory storage and retrieval.

key_press(event): Handles keyboard input and maps keys to respective functions.

User Interface:
Dynamic Button Grid: The buttons are created dynamically using a loop.

Responsive Design: The layout adjusts as per the window size.

Error Handling: Invalid expressions are caught and displayed as an error.

🧠 Future Enhancements
🔥 History Feature: Keep track of previous calculations.

🌐 Support for Additional Functions: Add more advanced mathematical operations.

🎨 Theme Customization: Allow users to switch between light and dark modes.

🙌 Credits
This project was developed by Mr. Aashish Tharu Gamuwa from Quantum University.
Feel free to fork the repository and contribute to improving the calculator!

💡 Thank You!
Enjoy using your very own Scientific Calculator! ✔️

