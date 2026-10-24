

\# Module templates — Interface utilisateur



\## 1. Rôle du module:



Le dossier `templates/` contient les modèles HTML utilisés par Flask pour générer l'interface web de la calculatrice.



Il permet de séparer la présentation de l'application de la logique Python définie dans `app.py`.



\## 2. Fichiers et responsabilités:



\### `index.html`



Ce fichier constitue l'interface principale de la calculatrice.



Il contient :

\- Un champ d'affichage de l'expression et du résultat.

\- Des boutons permettant de saisir les chiffres et les opérateurs.

\- Un formulaire HTML utilisant la méthode POST pour transmettre l'expression au serveur.

\- Deux fonctions JavaScript : `appendToDisplay()` pour ajouter un caractère et `clearDisplay()` pour effacer le champ.



Le template utilise la variable Jinja2 `{{ result }}` pour afficher le résultat transmis par Flask.



\## 3. Dépendances:



\- \*\*Flask (`app.py`)\*\* : traite les requêtes et génère la page HTML avec `render\_template()`.

\- \*\*Jinja2\*\* : permet d'insérer le résultat du calcul dans le template.

\- \*\*`static/style.css`\*\* : définit l'apparence graphique de la calculatrice.

\- \*\*JavaScript\*\* : permet de modifier le contenu du champ d'affichage côté navigateur.



\## 4. Hypothèses de fonctionnement:



\- L'interface est servie par Flask et ne doit pas être ouverte directement comme un fichier HTML autonome.

\- Le serveur transmet une variable `result` au template.

\- Le champ d'affichage est en lecture seule : la saisie se fait à l'aide des boutons.

\- Le calcul est effectué côté serveur lors de la soumission du formulaire.



