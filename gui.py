import tkinter as tk
from calculator import evaluate_expression, plot_graph

# ----------------------------
# MAIN WINDOW
# ----------------------------
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("400x800")
root.resizable(False, False)
root.configure(bg="#150404")

# ----------------------------
# GLOBAL VARIABLES
# ----------------------------
expression = ""
history = []
dark_mode = True
buttons = []

# ----------------------------
# DISPLAY FUNCTIONS
# ----------------------------
def update_display():
    display_var.set(expression)

def press(value):
    global expression
    expression += str(value)
    update_display()

def clear():
    global expression
    expression = ""
    update_display()

def backspace():
    global expression
    expression = expression[:-1]
    update_display()

def calculate():
    global expression

    result = evaluate_expression(expression)

    history.append(f"{expression} = {result}")
    update_history()

    expression = str(result)
    update_display()

def add_func(func):
    global expression
    expression += func + "("
    update_display()

def add_const(value):
    global expression
    expression += value
    update_display()

def graph(func):
    plot_graph(func)

# ----------------------------
# DISPLAY
# ----------------------------
display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)
display.pack(fill="both", ipadx=10, ipady=20, padx=10, pady=10)

# ----------------------------
# HISTORY BOX
# ----------------------------
history_box = tk.Text(
    root,
    height=6,
    bg="#111",
    fg="lightgray",
    font=("Arial", 10)
)
history_box.pack(fill="both", padx=10, pady=5)

def update_history():
    history_box.delete("1.0", tk.END)

    for item in history[-10:]:
        history_box.insert(tk.END, item + "\n")

# ----------------------------
# THEME TOGGLE
# ----------------------------
def toggle_theme():
    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:
        root.configure(bg="#150404")
        frame.configure(bg="#0f0f0f")

        display.configure(
            bg="#1e1e1e",
            fg="white",
            insertbackground="white"
        )

        history_box.configure(
            bg="#111111",
            fg="lightgray"
        )

        for b in buttons:
            b.configure(fg="white")

        theme_btn.configure(text="☀ Light Mode")

    else:
        root.configure(bg="#f5f5f5")
        frame.configure(bg="#e0e0e0")

        display.configure(
            bg="white",
            fg="black",
            insertbackground="black"
        )

        history_box.configure(
            bg="white",
            fg="black"
        )

        for b in buttons:
            b.configure(fg="white")

        theme_btn.configure(text="🌙 Dark Mode")

# ----------------------------
# BUTTON FRAME
# ----------------------------
frame = tk.Frame(root, bg="#0f0f0f")
frame.pack()

# ----------------------------
# BUTTON CREATOR
# ----------------------------
def btn(text, row, col, cmd, bg="#2c2c2c"):
    b = tk.Button(
        frame,
        text=text,
        command=cmd,
        width=7,
        height=2,
        font=("Arial", 12),
        bg=bg,
        fg="white",
        activebackground="#444",
        bd=0
    )

    b.grid(row=row, column=col, padx=3, pady=3)
    buttons.append(b)

# ----------------------------
# BASIC ROWS
# ----------------------------
btn("C", 0, 0, clear, "#c62828")
btn("⌫", 0, 1, backspace, "#ef6c00")
btn("(", 0, 2, lambda: press("("))
btn(")", 0, 3, lambda: press(")"))

btn("7", 1, 0, lambda: press("7"))
btn("8", 1, 1, lambda: press("8"))
btn("9", 1, 2, lambda: press("9"))
btn("/", 1, 3, lambda: press("/"))

btn("4", 2, 0, lambda: press("4"))
btn("5", 2, 1, lambda: press("5"))
btn("6", 2, 2, lambda: press("6"))
btn("*", 2, 3, lambda: press("*"))

btn("1", 3, 0, lambda: press("1"))
btn("2", 3, 1, lambda: press("2"))
btn("3", 3, 2, lambda: press("3"))
btn("-", 3, 3, lambda: press("-"))

btn("0", 4, 0, lambda: press("0"))
btn(".", 4, 1, lambda: press("."))
btn("=", 4, 2, calculate, "#2e7d32")
btn("+", 4, 3, lambda: press("+"))

# ----------------------------
# SCIENTIFIC ROW
# ----------------------------
btn("sin", 5, 0, lambda: add_func("sin"))
btn("cos", 5, 1, lambda: add_func("cos"))
btn("tan", 5, 2, lambda: add_func("tan"))
btn("√", 5, 3, lambda: add_func("sqrt"))

btn("log", 6, 0, lambda: add_func("log"))
btn("ln", 6, 1, lambda: add_func("ln"))
btn("x!", 6, 2, lambda: add_func("factorial"))
btn("^", 6, 3, lambda: press("**"))

# ----------------------------
# CONSTANTS
# ----------------------------
btn("π", 7, 0, lambda: add_const("pi()"))
btn("e", 7, 1, lambda: add_const("e()"))
btn("x²",7, 2, lambda: graph("x2"), "#6d4c41")
btn("x³",7, 3, lambda: graph("x3"), "#6d4c41")

# ----------------------------
# GRAPHS
# ----------------------------
btn("sin(x)", 8, 0, lambda: graph("sin"), "#3949ab")
btn("cos(x)", 8, 1, lambda: graph("cos"), "#3949ab")
btn("tan(x)", 8, 2, lambda: graph("tan"), "#3949ab")
btn("√x"    , 8, 3, lambda: graph("sqrt"), "#6d4c41")

# ----------------------------
# THEME BUTTON
# ----------------------------
theme_btn = tk.Button(
    root,
    text="☀ Light Mode",
    command=toggle_theme,
    font=("Arial", 12, "bold"),
    bg="#2196f3",
    fg="white",
    bd=0,
    pady=8
)

theme_btn.pack(fill="x", padx=10, pady=10)

# ----------------------------
# RUN APP
# ----------------------------
root.mainloop()

