# Scrapping-adresses-mairies.fr
Ce projet est un simple scrapper Python du site adresses-mairies.fr permettant de récupérer les n° de téléphone et mails d'un département donné.

## Utilisation
### Installation de Python et pip
Le script fonctionnant avec Python, il faut tout d'abord installer celui-ci.
Pour cela, cliquez [ici](https://www.python.org/downloads/). Veuillez à bien sélectionner votre OS (Windows, Mac ou UNIX).

Il faudra ensuite installer l'outil [pip](https://pip.pypa.io/en/stable/) qui est un gestionnaire de paquets permettant d'ajouter des fonctionnalités à notre programme.
Pour cela, cliquez [ici](https://pip.pypa.io/en/stable/installation/). Veuillez à bien sélectionner la procédure pour votre OS (Windows, Mac ou UNIX).

### Installation des paquets
Une fois Python et pip installés, lancez votre ligne de commandes (Windows : `⊞ Win + R` et tapez "cmd" puis entrer).
Dans le terminal, entrez :
```bash
pip install requests
pip install beautifulsoup4
pip install regex
pip install XlsxWriter
```

### Script
Pour éviter de devoir retaper les départements souhaités, j'ai opté pour une liste en dur dans le code.
Cette liste appelée `départements` prend comme éléments une autre liste au format ["*code_departement* - *nom_département*", "*url_département*"].
Ouvrez le fichier (avec l'application bloc-notes par exemple) et insérez les départements souhaitez.

**Exemples**
```bash
departements = [["75 - Paris", "https://www.adresses-mairies.fr/departement-paris-76.html"]] # Scrapping des mairies de Paris
departements = [["75 - Paris", "https://www.adresses-mairies.fr/departement-paris-76.html"], ["77 - Seine-et-Marne", "https://www.adresses-mairies.fr/departement-seine-et-marne-78.html"], ["78 - Yvelines", "https://www.adresses-mairies.fr/departement-yvelines-79.html"]] # Scrapping des mairies de Paris, de Seine-et-Marne et des Yvelines
departements = [["77 - Seine-et-Marne", "https://www.adresses-mairies.fr/departement-seine-et-marne-78.html"], ["95 - Val d'Oise", "https://www.adresses-mairies.fr/departement-val-d-oise-96.html"]] # Scrapping des mairies de Seine-et-Marne et du Val d'Oisie

```
