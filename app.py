"""Serveur Flask et analyse d'expressions de la calculatrice.

Le serveur délègue les opérations élémentaires au module operators.
Il rend le template HTML depuis templates/ et sert le CSS depuis static/.
"""
import re
from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)
# Pour centraliser la correspondance entre symboles saisis et fonctions à appeler.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Role:
        Analyse et calcule une expression contenant plusieurs opérations.
        La multiplication et la division sont prioritaires sur l'addition et
        la soustraction; les opérations de même priorité sont évaluées de
        gauche à droite.
    Args:
        expr (str): Expression envoyée par le formulaire, p. ex:(8 + 3).
    Returns:
    float: Résultat de l'expression.
    Raises:
    ValueError: Si l'expression est vide, mal formée ou contient
        des opérandes non numériques.
        ZeroDivisionError: Si la fonction de division reçoit un diviseur nul.
    """
    if not isinstance(expr, str) or not expr.strip():
        raise ValueError("empty expression")

    token_pattern = re.compile(r"\s*(?:(\d+(?:\.\d*)?|\.\d+)|([+\-*/]))")
    tokens = []
    position = 0

    while position < len(expr):
        if not expr[position:].strip():
            break

        match = token_pattern.match(expr, position)
        if match is None:
            raise ValueError("invalid expression format")

        number, operator = match.groups()
        tokens.append(float(number) if number is not None else operator)
        position = match.end()

    token_position = 0
    binary_operator_count = 0

    def parse_factor():
        nonlocal token_position
        sign = 1

        while (
            token_position < len(tokens)
            and tokens[token_position] in ("+", "-")
        ):
            if tokens[token_position] == "-":
                sign *= -1
            token_position += 1

        if (
            token_position >= len(tokens)
            or isinstance(tokens[token_position], str)
        ):
            raise ValueError("invalid expression format")

        value = tokens[token_position]
        token_position += 1
        return sign * value

    def parse_term():
        nonlocal token_position, binary_operator_count
        value = parse_factor()

        while (
            token_position < len(tokens)
            and tokens[token_position] in ("*", "/")
        ):
            operator = tokens[token_position]
            token_position += 1
            right = parse_factor()
            binary_operator_count += 1
            value = OPS[operator](value, right)

        return value

    def parse_expression():
        nonlocal token_position, binary_operator_count
        value = parse_term()

        while (
            token_position < len(tokens)
            and tokens[token_position] in ("+", "-")
        ):
            operator = tokens[token_position]
            token_position += 1
            right = parse_term()
            binary_operator_count += 1
            value = OPS[operator](value, right)

        return value

    result = parse_expression()
    if token_position != len(tokens) or binary_operator_count == 0:
        raise ValueError("invalid expression format")

    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Role:
        Affiche la calculatrice et traite les expressions soumises.
    Entrées:
        Requête HTTP GET, ou POST dont le formulaire contient (display).
    Returns:
        str: Réponse HTML produite avec le template index.html, contenant
        le résultat de l'opération ou un message d'erreur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Le message est rendu dans l'interface au lieu d'interrompre la requête.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Le mode debug est prévu pour l'exécution locale, pas pour un déploiement public.
    app.run(debug=True)