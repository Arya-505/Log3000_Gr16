
"""Tests de l'analyse des expressions et des routes Flask."""

import pytest

from app import app, calculate


@pytest.fixture
def client():
    """
    Role:
        Fournit un client HTTP Flask pour tester les routes sans serveur réel.
    Args:
        Aucun.
    Yields:
        FlaskClient: Client de test permettant de simuler des requêtes HTTP.
    """
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("3+4", 7.0),
        (" 3 + 4 ", 7.0),
        ("8-3", 5.0),
        ("3*4", 12.0),
        ("7/2", 3.5),
    ],
)
def test_calculate_valid(expression, expected):
    """
    Role:
        Vérifie que calculate() évalue correctement une expression valide.
    Args:
        expression (str): Expression arithmétique à évaluer.
        expected (float): Résultat mathématique attendu.
    Returns:
        None: Le test réussit si le résultat correspond à expected.
    """
    assert calculate(expression) == pytest.approx(expected)


@pytest.mark.parametrize(
    "expression",
    [
        "",
        "3+",
        "+3",
        "3+4+5",
        "abc+2",
        "12",
    ],
)
def test_calculate_invalid(expression):
    """
    Role:
        Vérifie que calculate() rejette les expressions invalides.
    Args:
        expression (str): Expression vide, mal formée ou non valide.
    Returns:
        None: Le test réussit si ValueError est levée.
    """
    with pytest.raises(ValueError):
        calculate(expression)


def test_homepage_get(client):
    """
    Role:
        Vérifie que la page principale est accessible par une requête GET.
    Args:
        client (FlaskClient): Client de test Flask fourni par la fixture.
    Returns:
        None: Le test réussit si le statut HTTP est 200
        et si le titre de l'application est présent.
    """
    response = client.get("/")

    assert response.status_code == 200
    assert b"Flask Calculator" in response.data


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("3+4", "7.0"),
        ("8-3", "5.0"),
        ("3*4", "12.0"),
        ("7/2", "3.5"),
    ],
)
def test_homepage_post_calculation(client, expression, expected):
    """
    Role:
        Vérifie l'affichage du résultat après soumission du formulaire.
    Args:
        client (FlaskClient): Client de test simulant une requête POST.
        expression (str): Expression envoyée au serveur Flask.
        expected (str): Résultat attendu dans le champ d'affichage HTML.
    Returns:
        None: Le test réussit si le statut HTTP est 200
        et si le champ d'affichage contient le résultat attendu.
    """
    response = client.post("/", data={"display": expression})

    assert response.status_code == 200

    # Vérifier la valeur du champ, pas seulement la présence du nombre.
    assert f'value="{expected}"'.encode() in response.data


def test_homepage_post_invalid(client):
    """
    Role:
        Vérifie l'affichage d'un message pour une expression invalide.
    Args:
        client (FlaskClient): Client de test Flask.
    Returns:
        None: Le test réussit si le serveur répond avec le statut 200
        et affiche un message commençant par "Error:".
    """
    response = client.post("/", data={"display": "abc+2"})

    assert response.status_code == 200
    assert b"Error:" in response.data


def test_homepage_post_zero_division(client):
    """
    Role:
        Vérifie que l'interface signale une division par zéro.
    Args:
        client (FlaskClient): Client de test Flask.
    Returns:
        None: Le test réussit si un message d'erreur est affiché
        après une tentative de division par zéro.
    """
    response = client.post("/", data={"display": "5/0"})

    assert response.status_code == 200
    assert b"Error:" in response.data


def test_css_accessible(client):
    """
    Role:
        Vérifie que la feuille de style est accessible via Flask.
    Args:
        client (FlaskClient): Client de test Flask.
    Returns:
        None: Le test réussit si le fichier CSS est accessible
        et contient la classe principale de la calculatrice.
    """
    response = client.get("/static/style.css")

    assert response.status_code == 200
    assert b".calculator" in response.data
