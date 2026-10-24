
# Module de tests — Flask Calculator

## 1. Objectif

Le dossier `tests/` regroupe les tests automatisés de la calculatrice Flask.

Les tests vérifient la conformité de l'application avec son comportement attendu et permettent de détecter les bogues avant leur correction.

## 2. Fichiers et responsabilités

### `test_operators.py`

Tests unitaires des fonctions arithmétiques :
- Addition.
- Soustraction.
- Multiplication.
- Division.
- Division par zéro.

### `test_app.py`

Tests du backend et de l'intégration Flask :
- Analyse des expressions valides.
- Rejet des expressions invalides.
- Requêtes HTTP GET et POST.
- Affichage des résultats et messages d'erreur.
- Accessibilité de la feuille CSS.

### `test_interface.py`

Tests de l'interface HTML :
- Libellés des boutons et correspondance avec leurs actions.
- Méthode POST du formulaire.
- Présence du champ d'affichage en lecture seule.
- Présence des boutons de validation et d'effacement.

## 3. Dépendances et hypothèses

- Python, Flask et pytest sont nécessaires.
- Les dépendances sont déclarées dans `requirements.txt`.
- Les tests sont exécutés depuis le dossier principal du projet.
- Les résultats attendus suivent les spécifications de la calculatrice et les docstrings.
- Les tests peuvent échouer volontairement lorsque le code initial présente un bogue.

## 4. Exécution des tests

Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

Exécuter tous les tests :

```bash
python -m pytest -v
```

Exécuter les tests d'un module :

```bash
python -m pytest tests/test_operators.py -v
python -m pytest tests/test_app.py -v
python -m pytest tests/test_interface.py -v
```

Afficher des traces d'erreur plus courtes :

```bash
python -m pytest -v --tb=short
```

## 5. Interprétation des résultats

- `PASSED` : test réussi.
- `FAILED` : résultat obtenu différent du résultat attendu.
- `ERROR` : problème survenu pendant l'exécution ou la préparation du test.

Les échecs sont analysés pour identifier les bogues réels.

Chaque bogue confirmé est documenté dans une GitHub Issue avec :
- Une description du problème.
- Le comportement attendu.
- Le comportement observé.
- Les étapes de reproduction ou les cas de tests échoués.
- Un membre de l'équipe assigné.

## 6. Suivi des bogues

Les bogues ne sont pas corrigés dans la partie 3.

Les corrections seront réalises dans la partie 4, chacune sur une branche associée à une Issue.

Les tests concernés seront réexécutés après correction pour vérifier la résolution des problèmes.
