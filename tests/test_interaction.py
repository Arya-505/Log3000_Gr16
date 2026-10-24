"""Tests des interactions JavaScript de la calculatrice."""

import re
import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def run_javascript_display_test():
    """
    Prépare l'exécution du JavaScript de la calculatrice avec Node.js.

    Returns:
        Callable: Exécute une action et vérifie la valeur du champ display.
    """
    node = shutil.which("node")
    if node is None:
        pytest.fail("Node.js est requis pour les tests d'interaction.")

    template_path = (
        Path(__file__).resolve().parents[1] / "templates" / "index.html"
    )
    template = template_path.read_text(encoding="utf-8")
    script_match = re.search(r"<script>(.*?)</script>", template, re.DOTALL)
    assert script_match is not None, "Le script JavaScript est introuvable."
    javascript = script_match.group(1)

    def run_test(initial_value, action, expected_value):
        harness = f"""
const assert = require("node:assert/strict");
const vm = require("node:vm");
const display = {{ value: {initial_value!r} }};
const document = {{
  getElementById(id) {{
    assert.equal(id, "display");
    return display;
  }}
}};
const context = vm.createContext({{ assert, document, display }});
vm.runInContext(
  {f"{javascript}{action}assert.equal(display.value, {expected_value!r});"!r},
  context
);
"""
        result = subprocess.run(
            [node, "-e", harness],
            check=False,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stderr

    return run_test


def test_digit_button_replaces_calculation_result(run_javascript_display_test):
    """
    Vérifie qu'un chiffre efface le résultat précédent avant d'être affiché.
    """
    run_javascript_display_test("5.0", 'appendToDisplay("1");', "1")


def test_digit_button_replaces_error_message(run_javascript_display_test):
    """
    Vérifie qu'un chiffre efface le message d'erreur avant d'être affiché.
    """
    run_javascript_display_test(
        "Error: invalid expression",
        'appendToDisplay("1");',
        "1",
    )
