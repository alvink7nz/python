import re

class Compiler:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expression):
        tokens = re.findall(r'\d+|[-+*/()]|[a-zA-Z_]\w*', expression)
        postfix = self.infix_to_postfix(tokens)
        result = self.evaluate_postfix(postfix)
        return result

    def infix_to_postfix(self, infix):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operators = []

        for token in infix:
            if token.isdigit() or re.match(r'[a-zA-Z_]\w*', token):
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Discard the '('
            else:
                while operators and precedence.get(operators[-1], 0) >= precedence.get(token, 0):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        return output

    def evaluate_postfix(self, postfix):
        stack = []

        for token in postfix:
            if token.isdigit():
                stack.append(int(token))
            elif re.match(r'[a-zA-Z_]\w*', token):
                if token in self.variables:
                    stack.append(self.variables[token])
                else:
                    raise ValueError(f"Variable '{token}' is not defined.")
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    if operand2 != 0:
                        stack.append(operand1 / operand2)
                else:
                    raise ValueError("Division by zero.")
        if stack:
            return stack[0]
        else:
            raise ValueError("Expression is invalid.")

if __name__ == "__main__":
    compiler = Compiler()

    # Example usage:
    expression1 = "3 + 4 * 2 / ( 1 - 5 )"
    result1 = compiler.evaluate_expression(expression1)
    print(f"Result 1: {result1}")

    compiler.variables['x'] = 10
    expression2 = "x + 5"
    result2 = compiler.evaluate_expression(expression2)
    print(f"Result 2: {result2}")
