# Flask Calculator — LOG3000 TP3

**Équipe :** 16

## 1. Description et objectif du projet

Ce projet est une application web de calculatrice simple développée en Python avec le framework **Flask**.

Elle permet aux utilisateurs d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication et division) à travers une interface web intuitive.

Dans le cadre du TP3 du cours LOG3000, l'objectif est également de mettre en pratique les bonnes pratiques de gestion de versions et de développement collaboratif à l'aide de Git et GitHub.


### Portée du projet


L'application repose sur trois composants principaux :

- **Frontend :** HTML, CSS et JavaScript pour l'interface utilisateur.
- **Backend :** Flask pour recevoir les expressions, effectuer leur traitement et afficher les résultats.
- **Logique arithmétique :** `operators.py` pour les quatre opérations de base.

La calculatrice est conçue pour traiter des expressions contenant deux opérandes numériques et un seul opérateur arithmétique.

Elle ne prend pas en charge les expressions complexes, les parenthèses ou les calculs comportant plusieurs opérations.

La portée du projet est pédagogique : l'application ne nécessite ni système d'authentification ni base de données.

**Remarque :** la version initiale peut contenir des bogues qui seront identifiés par des tests et corrigés dans les prochaines parties du TP.


## 2. Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants :

- **Python** (version 3.10 ou supérieure)
- **pip** (gestionnaire de paquets Python)
- **Git** (outil de gestion des versions)

Les bibliothèques nécessaires sont indiquées dans `requirements.txt` :

- **Flask** : framework utilisé pour développer l'application web.
- **pytest** : framework utilisé pour exécuter les tests automatisés.

## 3. Instructions d'installation

### Étape 1 — Cloner le dépôt GitHub

```bash
git clone https://github.com/Arya-505/Log3000_Gr16.git
```

### Étape 2 — Accéder au dossier du projet

```bash
cd Log3000_Gr16
```

### Étape 3 — Créer un environnement virtuel (recommandé)

```bash
python -m venv .venv
```

### Étape 4 — Activer l'environnement virtuel

**Sur Windows (PowerShell) :**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Sur macOS/Linux :**

```bash
source .venv/bin/activate
```

### Étape 5 — Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

## 4. Instructions d'utilisation

### 4.1. Démarrer l'application

Depuis le dossier principal du projet, exécuter :

```bash
python app.py
```
Le serveur Flask démarre localement.

### 4.2. Accéder à la calculatrice

Ouvrir un navigateur web et accéder à l'adresse :

http://127.0.0.1:5000/

### 4.3. Effectuer un calcul

L'utilisateur peut effectuer un calcul en suivant ces étapes :

1. Cliquer sur les boutons numériques pour saisir le premier nombre.
2. Sélectionner un opérateur arithmétique : `+`, `-`, `*` ou `/`.
3. Saisir le deuxième nombre.
4. Cliquer sur le bouton `=` pour envoyer l'expression au serveur Flask.
5. Consulter le résultat affiché dans le champ de la calculatrice.
6. Cliquer sur `C` pour effacer le champ et effectuer un nouveau calcul.

**Exemple de fonctionnement attendu :**

Pour calculer `8 + 2` :

1. Cliquer sur `8`.
2. Cliquer sur `+`.
3. Cliquer sur `2`.
4. Cliquer sur `=`.

Le résultat attendu est `10.0`.

### 4.4. Gestion des expressions invalides

Le backend vérifie le format des expressions reçues.

Les expressions vides, mal formées, contenant plusieurs opérateurs ou des opérandes non numériques provoquent une erreur de validation.

La route Flask intercepte les erreurs de calcul et affiche un message dans l'interface.

Les comportements incorrects éventuels seront étudiés lors des tests automatisés.

### 4.5. Arrêter l'application

Dans le terminal exécutant Flask, appuyer sur :

`Ctrl + C`

## 5. Tests automatisés

Le projet utilise **pytest** pour vérifier le comportement attendu de la calculatrice.

Les tests seront regroupés dans le répertoire `tests/`.

Les tests des interactions JavaScript nécessitent également **Node.js**.

Ils permettront notamment de vérifier :

- Les quatre opérations arithmétiques.
- Les résultats attendus des calculs.
- La gestion des expressions invalides.
- Le traitement des erreurs.
- Le comportement de l'application Flask.

### 5.1. Exécuter les tests

Depuis le répertoire principal du projet, exécuter :

```bash
python -m pytest -v
```

L'option `-v` permet d'afficher le détail des tests exécutés et leurs résultats.

### 5.2. Interpréter les résultats

- **PASSED** : le test a réussi.
- **FAILED** : le comportement obtenu ne correspond pas au résultat attendu.
- **ERROR** : une erreur empêche l'exécution normale du test.

Les tests en échec seront analysés afin d'identifier les bogues et de créer les Issues GitHub correspondantes.

**État actuel :** les tests seront ajoutés dans la partie 3 du TP3. Cette section sera mise à jour après leur création.

## 6. Flux de contribution

Le projet utilise **Git et GitHub** pour organiser le développement collaboratif.

### 6.1. Gestion des branches

La branche `main` contient la version principale du projet.

Les modifications sont réalisées sur des branches dédiées afin de faciliter les revues de code et les fusions.

Les conventions de nommage sont les suivantes :

- `docs/description` : documentation.
- `test/description` : ajout de tests.
- `fix/description` : correction de bogues.
- `chore/description` : maintenance ou configuration.

Chaque correction de bogue doit être réalisée dans une branche distincte associée à une Issue GitHub.

### 6.2. Suivi des problèmes avec GitHub Issues

Lorsqu'un bogue est identifié, une Issue GitHub doit être créée.

Elle doit contenir :

- Une description claire du problème.
- Le comportement attendu.
- Le comportement observé.
- Les étapes permettant de reproduire le problème.
- Les tests en échec associés.
- Le membre de l'équipe responsable de la correction.

### 6.3. Enregistrement des modifications

Chaque modification est enregistrée avec un commit contenant un message explicite.

Exemples :

```bash
git commit -m "docs: ajout des docstrings"
git commit -m "test: ajout des tests de soustraction"
git commit -m "fix: correction de la soustraction"
```

### 6.4. Pull Requests

Pour proposer une modification :

1. Créer une branche dédiée depuis une version appropriée du projet.
2. Effectuer les modifications nécessaires.
3. Exécuter les tests concernés.
4. Enregistrer les changements avec un commit.
5. Pousser la branche sur GitHub.
6. Ouvrir une Pull Request vers `main`.
7. Décrire les changements effectués et demander une revue à un autre membre de l'équipe.
8. Fusionner la Pull Request après vérification.

### 6.5. Vérification après fusion

Après la fusion des corrections, l'ensemble de la suite de tests est exécuté afin de vérifier que les problèmes sont corrigés et qu'aucune régression n'a été introduite.

Les Issues correspondantes sont ensuite clôturées.

## 7. Structure du projet

```text
Log3000_Gr16/
├── app.py
├── operators.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   └── README.md
└── static/
    ├── style.css
    └── README.md
```

### Responsabilités des fichiers

- **`app.py`** : initialise le serveur Flask, analyse les expressions mathématiques et gère les requêtes HTTP.
- **`operators.py`** : contient les quatre fonctions arithmétiques utilisées par la calculatrice.
- **`requirements.txt`** : précise les dépendances Python nécessaires à l'application et aux tests.
- **`templates/index.html`** : définit l'interface utilisateur et les fonctions JavaScript.
- **`static/style.css`** : définit la présentation graphique de la calculatrice.

Les répertoires `templates/` et `static/` contiennent chacun un fichier `README.md` décrivant leur rôle, leurs principaux fichiers et leurs dépendances.

Un répertoire `tests/` et son fichier `README.md` seront ajoutés lors de la partie 3 du TP.
