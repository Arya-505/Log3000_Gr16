"""Serveur Flask et analyse d'expressions de la calculatrice.

Le serveur délègue les opérations élémentaires au module operators.
Il rend le template HTML depuis templates/ et sert le CSS depuis static/.
"""

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
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Refuse plusieurs symboles opérateurs : le parseur n'évalue pas de chaînes d'opérations.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        # Les deux opérandes doivent être présents de part et d'autre de l'opérateur.
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

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