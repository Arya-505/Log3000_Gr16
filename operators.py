"""Module des opérations arithmétiques de base de la calculatrice.

Ce module regroupe les fonctions d'addition, de soustraction,
de multiplication et de division utilisées par l'application Flask.
"""

# Les opérations sont séparées du serveur Flask pour pouvoir
# les tester indépendamment de l'interface web.

def add(a,b):
    """
    Role:
        Calcule la somme de deux nombres.
    Args:
        a (int | float): Premier opérande.
        b (int | float): Deuxième opérande.
    Returns:
        int | float: Somme de a et b.
    """
    return a + b

def subtract(a,b):
    """
    Role:
        Calcule la différence entre le premier et le second opérande.
    Args:
        a (int | float): Nombre auquel on soustrait b.
        b (int | float): Nombre à soustraire.
    Returns:
        int | float: Différence attendue a - b.
    """
    return a - b

def multiply(a,b):
    """
    Role:
        Calcule le produit de deux nombres.
    Args:
        a (int | float): Premier facteur.
        b (int | float): Deuxième facteur.
    Returns:
        int | float: Produit attendu a * b.
    """
    # Correction de 'a ** b' qui calcule l'exposant contre 'a * b' qui calcule la multiplication
    return a * b 

def divide(a,b):
    """
    Role:
        Calcule le quotient du premier opérande par le second.
    Args:
        a (int | float): Dividende.
        b (int | float): Diviseur non nul attendu.
    Returns:
        float: Quotient attendu a / b.
    Raises:
        ZeroDivisionError: Si le diviseur vaut zéro.
    """
    return a / b
