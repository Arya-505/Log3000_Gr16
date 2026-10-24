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
        Analyse une expression binaire puis délègue son calcul.
        Le format pris en charge par cette version est (nombre opérateur nombre)
        avec un seul opérateur parmi +, -, * et /.
    Args:
        expr (str): Expression envoyée par le formulaire, p. ex:(8 + 3).
    Returns:
        float: Résultat de l'opération appliquée à deux flottants.
    Raises:
        ValueError: Si l'expression est vide, mal formée, contient
            plusieurs opérateurs ou des opérandes non numériques.
        ZeroDivisionError: Si la fonction de division reçoit un diviseur nul.
    """
    if not isinstance(expr, str) or not expr.strip():
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    number = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)"
    pattern = rf"({number})([+\-*/])({number})"

    match = re.fullmatch(pattern, s)

    if match is None:
        raise ValueError("invalid expression format")

    left, operator, right = match.groups()

    a = float(left)
    b = float(right)

    return OPS[operator](a, b)

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