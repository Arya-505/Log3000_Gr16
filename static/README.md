

\# Module static — Styles de l'interface



\## 1. Rôle du module:



Le dossier `static/` contient les ressources statiques utilisées pour la présentation de l'application Flask.



Il sépare la mise en forme graphique de la structure HTML et de la logique métier Python.



\## 2. Fichiers et responsabilités:



\### `style.css`



Ce fichier définit l'apparence visuelle de la calculatrice.



Il gère notamment :

\- Le centrage de la calculatrice sur la page.

\- Les couleurs, les dimensions et les bordures des éléments.

\- La présentation du champ d'affichage.

\- La disposition des boutons dans une grille de quatre colonnes.

\- La distinction visuelle des boutons opérateurs.

\- Les effets visuels lors du survol et du clic sur les boutons.



Les principales classes CSS utilisées sont :

\- `.calculator` : conteneur principal.

\- `.buttons` : grille des boutons.

\- `.btn` : style commun des boutons.

\- `.operator` : style spécifique des opérateurs.



\## 3. Dépendances:



\- \*\*`templates/index.html`\*\* : utilise les classes CSS définies dans `style.css`.

\- \*\*Flask\*\* : fournit les ressources du dossier `static/` au navigateur.



Le fichier CSS est chargé dans `index.html` avec :



`{{ url\_for('static', filename='style.css') }}`



\## 4. Hypothèses de fonctionnement:



\- Le fichier CSS doit être situé dans le dossier `static/` reconnu par Flask.

\- Le template HTML doit utiliser les noms de classes CSS correspondants.

\- Le navigateur doit pouvoir charger la feuille de style.

\- Les styles modifient uniquement la présentation et ne réalisent aucun calcul arithmétique.



