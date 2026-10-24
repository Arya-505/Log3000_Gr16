
"""Tests unitaires des opérations arithmétiques de la calculatrice."""

import pytest

from operators import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 7),
        (0, 5, 5),
        (-2, 3, 1),
    ],
)
def test_add(a, b, expected):
    """
    Role:
        Vérifie que l'addition retourne la somme a + b.
    Args:
        a (int): Premier opérande.
        b (int): Deuxième opérande.
        expected (int): Résultat attendu.
    Returns:
        None: Le test réussit si le résultat est correct.
    """
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (8, 2, 6),
        (3, 8, -5),
    ],
)
def test_subtract(a, b, expected):
    """
    Role;
        Vérifie que la soustraction retourne a - b.
    Args:
        a (int): Premier opérande.
        b (int): Deuxième opérande.
        expected (int): Résultat attendu.
    Returns:
        None: Le test réussit si le résultat est correct.
    """
    assert subtract(a, b) == expected

#Il permet d'exécuter une même fonction de test plusieurs fois avec des valeurs différentes
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 12),
        (5, 0, 0),
        (-2, 3, -6),
    ],
)
def test_multiply(a, b, expected):
    """
    Role:
        Vérifie que la multiplication retourne a * b.
    Args:
        a (int): Premier opérande.
        b (int): Deuxième opérande.
        expected (int): Résultat attendu.
    Returns:
        None: Le test réussit si le résultat est correct.
    """
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (7, 2, 3.5),
        (8, 4, 2.0),
        (-9, 2, -4.5),
    ],
)
def test_divide(a, b, expected):
    """
    Role:
        Vérifie que la division retourne le quotient réel a / b.
    Args:
        a (int): Numérateur.
        b (int): Dénominateur non nul.
        expected (float): Quotient attendu.
    Returns:
        None: Le test réussit si le quotient est correct.
    """
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    """
    Role:
        Vérifie qu'une division par zéro lève ZeroDivisionError.
    Args:
        Aucun.
    Returns:
        None: Le test réussit si l'exception attendue est levée.
    """
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
