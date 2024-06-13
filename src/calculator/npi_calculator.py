def eval_npi(expression: str) -> int:
    """
    

    Args:
        expression (str): _description_

    Returns:
        int: _description_
    """
    stack = []
    tokens = expression.split()  # Sépare l'expression en tokens (opérandes et opérateurs)

    for token in tokens:
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):
            # Si le token est un nombre (positif ou négatif)
            stack.append(int(token))
        else:
            # Sinon, c'est un opérateur
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)  # Attention à la division par zéro ici
            
    return stack.pop()  # Le résultat final se trouve au sommet de la pile

if __name__ == '__main__':
    # Exemples d'utilisation :
    print(eval_npi("3 4 +"))   # Résultat attendu : 7
    print(eval_npi("3 4 16 + *"))  # Résultat attendu : 60
    print(eval_npi("34 16 +"))  # Résultat attendu : 50
    print(eval_npi("3 416 +"))  # Résultat attendu : 419
    print(eval_npi("146 6 +"))  # Résultat attendu : 152
