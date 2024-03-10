import random

def generate_algebra_expression(variable='x', max_terms=3, max_coefficient=10, max_exponent=3):
    expression = ''
    num_terms = random.randint(1, max_terms)
    
    for _ in range(num_terms):
        coefficient = random.randint(1, max_coefficient)
        exponent = random.randint(1, max_exponent)
        if exponent == 1:
            term = f'{coefficient}{variable}'
        else:
            term = f'{coefficient}{variable}^{exponent}'
        
        expression += f'{term} + '
    
    # Remove the trailing ' + ' from the last term
    expression = expression[:-3]
    
    return expression

if __name__ == "__main__":
    for _ in range(5):  # Generate 5 random algebraic expressions
        print(generate_algebra_expression())