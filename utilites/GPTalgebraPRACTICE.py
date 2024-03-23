import numpy as np
from sympy import pprint

# Generate random coefficients and exponents
coefficients = np.random.randint(-10, 10, size=3)
exponents = np.random.randint(1, 5, size=3)

# Construct a random polynomial equation
def generate_random_equation(coefficients, exponents):
    terms = [f"{coeff}*x**{exp}" for coeff, exp in zip(coefficients, exponents)]
    return " + ".join(terms)

equation = generate_random_equation(coefficients, exponents)
pprint(equation)