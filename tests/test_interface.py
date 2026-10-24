
"""Tests de la structure HTML et des boutons de la calculatrice."""

from html.parser import HTMLParser

import pytest

from app import app


class InterfaceParser(HTMLParser):
    """
    Role:
        Analyse le HTML pour extraire les informations utiles aux tests.
    Attributes:
        buttons (list): Liste des boutons et de leurs attributs.
        inputs (list): Liste des champs de saisie HTML.
        forms (list): Liste des formulaires HTML.
        current_button (dict | None): Bouton en cours d'analyse.
    """

    def __init__(self):
        """
        Role:
            Initialise les collections utilisées pendant l'analyse HTML.
        Args:
            Aucun.
        Returns:
            None: Initialise les attributs de l'objet.
        """
        super().__init__()
        self.buttons = []
        self.inputs = []
        self.forms = []
        self.current_button = None

    def handle_starttag(self, tag, attrs):
        """
        Role:
            Enregistre les attributs des éléments HTML utiles aux tests.
        Args:
            tag (str): Nom de la balise HTML rencontrée.
            attrs (list): Liste des attributs de la balise.
        Returns:
            None: Met à jour les collections internes du parseur.
        """
        attributes = dict(attrs)

        if tag == "form":
            self.forms.append(attributes)

        elif tag == "input":
            self.inputs.append(attributes)

        elif tag == "button":
            self.current_button = {
                "onclick": attributes.get("onclick", ""),
                "type": attributes.get("type", ""),
                "label": "",
            }

    def handle_data(self, data):
        """
        Role:
            Récupère le texte affiché dans le bouton en cours d'analyse.
        Args:
            data (str): Texte rencontré entre les balises HTML.
        Returns:
            None: Ajoute le texte au libellé du bouton courant.
        """
        if self.current_button is not None:
            self.current_button["label"] += data

    def handle_endtag(self, tag):
        """
        Role:
            Termine l'analyse d'un bouton et l'ajoute à la liste.
        Args:
            tag (str): Nom de la balise HTML fermante.
        Returns:
            None: Enregistre le bouton et réinitialise son état.
        """
        if tag == "button" and self.current_button is not None:
            self.current_button["label"] = (
                self.current_button["label"].strip()
            )
            self.buttons.append(self.current_button)
            self.current_button = None


@pytest.fixture
def interface():
    """
    Role:
        Prépare l'interface HTML pour les tests.
    Args:
        Aucun.
    Returns:
        InterfaceParser: Objet contenant les informations
        extraites de la page principale de Flask.
    """
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200

    parser = InterfaceParser()
    parser.feed(response.get_data(as_text=True))
    return parser

#Il permet de lancer le même test plusieurs fois avec des valeurs différentes.
@pytest.mark.parametrize(
    "value, expected_label",
    [
        ("1", "1"),
        ("2", "2"),
        ("8", "8"),
        ("*", "*"),
        ("/", "/"),
    ],
)
def test_button_label(interface, value, expected_label):
    """
    Role:
        Vérifie que le texte visible d'un bouton correspond à son action.
    Args:
        interface (InterfaceParser): Interface HTML analysée.
        value (str): Caractère inséré par le bouton.
        expected_label (str): Texte attendu sur le bouton.
    Returns:
        None: Le test réussit si le bon libellé est affiché.
    """
    action = f"appendToDisplay('{value}')"

    # L'action permet d'identifier précisément le bouton à vérifier.
    matching = [
        button for button in interface.buttons
        if button["onclick"] == action
    ]

    assert len(matching) == 1
    assert matching[0]["label"] == expected_label


def test_form_uses_post(interface):
    """
    Role:
        Vérifie que le formulaire HTML utilise la méthode POST.
    Args:
        interface (InterfaceParser): Interface HTML analysée.
    Returns:
        None: Le test réussit si un formulaire utilise POST.
    """
    assert any(
        form.get("method", "").upper() == "POST"
        for form in interface.forms
    )


def test_display_readonly(interface):
    """
    Role:
        Vérifie que le champ d'affichage ne permet pas la saisie directe.
    Args:
        interface (InterfaceParser): Interface HTML analysée.
    Returns:
        None: Le test réussit si le champ display est en lecture seule.
    """
    assert any(
        field.get("id") == "display"
        and field.get("name") == "display"
        and "readonly" in field
        for field in interface.inputs
    )


def test_equals_button(interface):
    """
    Role:
        Vérifie que le bouton égal soumet le formulaire.
    Args:
        interface (InterfaceParser): Interface HTML analysée.
    Returns:
        None: Le test réussit si le bouton égal est de type submit.
    """
    assert any(
        button["label"] == "="
        and button["type"] == "submit"
        for button in interface.buttons
    )


def test_clear_button(interface):
    """
    Role:
        Vérifie la présence et l'action du bouton d'effacement.
    Args:
        interface (InterfaceParser): Interface HTML analysée.
    Returns:
        None: Le test réussit si le bouton C appelle clearDisplay().
    """
    assert any(
        button["label"] == "C"
        and button["onclick"] == "clearDisplay()"
        for button in interface.buttons
    )
