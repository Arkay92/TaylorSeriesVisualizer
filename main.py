import math
import matplotlib.pyplot as plt

def factorial(n):
    """Return the factorial of n, used in the denominator of Taylor series terms."""
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)

def taylor_series_approximation(func, derivative_funcs, a, x, n_terms):
    """General function to approximate a given function at x using n terms of its Taylor series around a point a."""
    approximation = 0
    for n in range(n_terms):
        try:
            derivative_at_a = derivative_funcs[n](a)
        except IndexError:
            print(f"Error: Derivative function for n={n} is missing.")
            break
        term = derivative_at_a * ((x - a)**n) / factorial(n)
        approximation += term
    return approximation

def calculate_error(actual_value, approximated_value):
    """Calculate the absolute error between the actual function value and the Taylor series approximation."""
    return abs(actual_value - approximated_value)

def plot_function_and_approximation(func, approx_func, a, x_range, n_terms):
    """Plot the original function and its Taylor series approximation to visualize the accuracy."""
    x_values = [x / 100.0 for x in range(int(x_range[0] * 100), int(x_range[1] * 100))]
    y_actual = [func(x) for x in x_values]
    y_approx = [approx_func(func, derivative_funcs, a, x, n_terms) for x in x_values]

    plt.plot(x_values, y_actual, label="Actual Function")
    plt.plot(x_values, y_approx, label="Taylor Series Approximation", linestyle='--')
    plt.axvline(x=a, color='r', linestyle=':', label="Point of Expansion")
    plt.title("Function and its Taylor Series Approximation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage with e^x, where all derivatives are e^x
def e_x(x):
    """The exponential function e^x."""
    return math.exp(x)

# List of derivative functions for e^x
derivative_funcs = [lambda x: math.exp(x) for _ in range(10)]

# User inputs
a = 0  # Point of expansion
x = 1  # Point to approximate
n_terms = 5  # Number of terms in the Taylor series

# Approximation and error calculation
approx_value = taylor_series_approximation(e_x, derivative_funcs, a, x, n_terms)
actual_value = e_x(x)
error = calculate_error(actual_value, approx_value)

print(f"Approximated value of e^x at x={x} using {n_terms} terms: {approx_value}")
print(f"Actual value of e^x at x={x}: {actual_value}")
print(f"Absolute error: {error}")

# Visualization
plot_function_and_approximation(e_x, taylor_series_approximation, a, (-2, 2), n_terms)
