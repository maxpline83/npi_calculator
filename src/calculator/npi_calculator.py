def eval_npi(expression: str) -> int:
    """
    Evaluate an expression in Reverse Polish Notation (RPN) and return the result.

    Args:
        expression (str): A string representing the expression in Reverse Polish Notation.

    Raises:
        ZeroDivisionError: Raised when division by zero is encountered.
        ValueError: Raised when an invalid token is encountered.
        IndexError: Raised when the expression is invalid.

    Returns:
        int: The result of the evaluated expression.

    Example:
        >>> eval_npi("5 3 +")
        8
        >>> eval_npi("4 2 * 3 +")
        11
        >>> eval_npi("10 2 /")
        5
    """
    stack = []
    tokens = expression.split(" ")

    for token in tokens:
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):
            stack.append(int(token))
        elif token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                else:
                    stack.append(operand1 / operand2)
        else:
            raise ValueError(f"Invalid token: {token}, only numbers and operators are allowed")
    if len(stack) == 1:
        return stack.pop()
    else:
        raise IndexError("Invalid expression")


if __name__ == '__main__':
    print(eval_npi("3 10 5 + *")) # Expected output: 45