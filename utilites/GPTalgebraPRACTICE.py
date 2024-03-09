from sympy import symbols, Eq, solve
import random

# Define the symbol
x = symbols('x')

def generateQuestion():
    # Generate random coefficients and constants
    a, b, c, d = [random.randint(-10, 10) for _ in range(4)]
    
    # Generate the equation
    equation = f"{a}*x / {b} = {c}*x + {d}"
    
    return equation

def rightAnswer(equation_str):
    # Split the equation string into its components
    equation_parts = equation_str.split('=')
    
    try:
        # Create the equation using Eq
        lhs = eval(equation_parts[0].strip())  # Evaluate the left-hand side
        rhs = eval(equation_parts[1].strip())  # Evaluate the right-hand side
        equation = Eq(lhs, rhs)
        
        # Solve the equation
        answer = solve(equation, x)
        
        return answer
    except Exception as e:
        print("Error:", e)
        return None

# Generate a random question
question = generateQuestion()

# Get the correct answer
correct_answer = rightAnswer(question)
print("Question:", question)
print("Correct Answer:", correct_answer)
