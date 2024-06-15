def eval_npi(expression: str) -> float:
    """
    Evaluate an expression in Reverse Polish Notation (RPN) and return the result.

    Args:
        expression (str): A string representing the expression in Reverse Polish Notation.

    Raises:
        ZeroDivisionError: Raised when division by zero is encountered.
        ValueError: Raised when an error if the expression is invalid.

    Returns:
        int: The result of the evaluated expression.

    Example:
        >>> eval_npi("5 3 +")
        8
        >>> eval_npi("4 2 * 3 +")
        11
        >>> eval_npi("10 2 ÷")
        5.0
    """

    is_valid, error_message = validate_rpn(expression)
    if not is_valid:
        raise ValueError(error_message)
    
    stack = []
    tokens = expression.split(" ")

    for token in tokens:
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):
            stack.append(int(token))
        elif token in ['+', '-', '*', '÷']:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '÷':
                if operand2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                else:
                    stack.append(operand1 / operand2)
    return stack.pop()

def validate_rpn(expression: str) -> tuple:
    """
    Validate an expression in Reverse Polish Notation (RPN).

    Args:
        expression (str): A string representing the expression in Reverse Polish Notation.

    Returns:
        tuple: (True, "") if the expression is valid, (False, error message) if invalid.
    """
    stack = []
    tokens = expression.split(" ")

    for token in tokens:
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):
            stack.append(token)
        elif token in ['+', '-', '*', '÷']:
            if len(stack) < 2:
                return False, f"Error: not enough operands for operator '{token}'"
            stack.pop()
            stack.pop()
            stack.append('1')
        else:
            return False, f"Error: invalid token '{token}'"

    if len(stack) != 1:
        return False, "Error: invalid expression, final stack size is not 1"

    return True, ""
if __name__ == '__main__':
    print(eval_npi("3 10 5 + *"))  # Expected output: 45.0
    print(eval_npi("3 4 2 + + +")) # Expected output: 7.0
