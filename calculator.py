import math
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# BASIC OPERATIONS
# =========================================================

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

def power(a, b): return a ** b
def modulus(a, b): return a % b


# =========================================================
# SCIENTIFIC FUNCTIONS (DEGREE BASED)
# =========================================================

def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))

def sinh(x): return math.sinh(x)
def cosh(x): return math.cosh(x)
def tanh(x): return math.tanh(x)

def sqrt(x):
    if x < 0:
        return "Error"
    return math.sqrt(x)

def log(x):
    if x <= 0:
        return "Error"
    return math.log10(x)

def ln(x):
    if x <= 0:
        return "Error"
    return math.log(x)

def factorial(x):
    if x < 0:
        return "Error"
    return math.factorial(int(x))


# =========================================================
# CONSTANTS
# =========================================================

def pi(): return math.pi
def e(): return math.e


# =========================================================
# SAFE EXPRESSION EVALUATION ENGINE
# =========================================================

def evaluate_expression(expression):

    allowed = {
        "__builtins__": {},

        # functions
        "sin": sin,
        "cos": cos,
        "tan": tan,
        "sqrt": sqrt,
        "log": log,
        "ln": ln,
        "factorial": factorial,

        # constants
        "pi": pi,
        "e": e,

        # python safe functions
        "abs": abs,
        "round": round,
        "pow": pow,
    }

    try:
        return eval(expression, allowed, {})
    except:
        return "Error"


# =========================================================
# GRAPH PLOTTING ENGINE
# =========================================================

def plot_graph(func_name):
    """
    Plots mathematical functions
    """

    x = np.linspace(-10, 10, 1000)

    try:
        if func_name == "sin":
            y = np.sin(np.radians(x))
        elif func_name == "cos":
            y = np.cos(np.radians(x))
        elif func_name == "tan":
            y = np.tan(np.radians(x))
        elif func_name == "sqrt":
            y = np.sqrt(np.abs(x))
        elif func_name == "x2":
            y = x ** 2
        elif func_name == "x3":
            y = x ** 3
        else:
            y = x

        plt.figure(figsize=(6, 4))
        plt.plot(x, y)
        plt.title(f"Graph of {func_name}(x)")
        plt.grid(True)
        plt.show()

    except Exception as e:
        print("Graph Error:", e)