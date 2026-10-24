# Flask Calculator — LOG3000 TP3

**Équipe :** 16

## 1. Description et objectif du projet

Ce projet est une application web de calculatrice simple développée en Python avec le framework **Flask**.

Elle permet aux utilisateurs d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication et division) à travers une interface web intuitive.

Dans le cadre du TP3 du cours LOG3000, l'objectif est également de mettre en pratique les bonnes pratiques de gestion de versions et de développement collaboratif à l'aide de Git et GitHub.

La portée du projet est pédagogique : l'application ne nécessite ni système d'authentification ni base de données.

## 2. Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants :

- **Python** (version 3.10 ou supérieure)
- **pip** (gestionnaire de paquets Python)
- **Git** (outil de gestion des versions)

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

### Étape 6 — Lancer l'application

```bash
python app.py
```

### Étape 7 — Accéder à la calculatrice

Ouvrir un navigateur web et accéder à l'adresse suivante :

http://127.0.0.1:5000/