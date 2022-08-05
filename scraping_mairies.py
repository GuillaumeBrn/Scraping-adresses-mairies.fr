import requests
from bs4 import BeautifulSoup
import re
import xlsxwriter 
from datetime import datetime


# Rajouter entre [] le code et le nom du département (ce sera le nom de la feuille Excel) + l'URL du département sur adresses-mairies.fr
# departements = [["75 - Paris", "https://www.adresses-mairies.fr/departement-paris-76.html"], ["77 - Seine-et-Marne", "https://www.adresses-mairies.fr/departement-seine-et-marne-78.html"], ["78 - Yvelines", "https://www.adresses-mairies.fr/departement-yvelines-79.html"], ["91 - Essonne", "https://www.adresses-mairies.fr/departement-essonne-92.html"], ["92 - Hauts-de-Seine", "https://www.adresses-mairies.fr/departement-hauts-de-seine-93.html"], ["93 - Seine-Saint-Denis", "https://www.adresses-mairies.fr/departement-seine-saint-denis-94.html"], ["94 - Val-de-Marne", "https://www.adresses-mairies.fr/departement-val-de-marne-95.html"], ["95 - Val d'Oise", "https://www.adresses-mairies.fr/departement-val-d-oise-96.html"]]
# departements = [["75 - Paris", "https://www.adresses-mairies.fr/departement-paris-76.html"]] # scraping des mairies de Paris
# departements = [["75 - Paris", "https://www.adresses-mairies.fr/departement-paris-76.html"], ["77 - Seine-et-Marne", "https://www.adresses-mairies.fr/departement-seine-et-marne-78.html"], ["78 - Yvelines", "https://www.adresses-mairies.fr/departement-yvelines-79.html"]] # scraping des mairies de Paris, de Seine-et-Marne et des Yvelines
# departements = [["77 - Seine-et-Marne", "https://www.adresses-mairies.fr/departement-seine-et-marne-78.html"], ["95 - Val d'Oise", "https://www.adresses-mairies.fr/departement-val-d-oise-96.html"]] # scraping des mairies de Seine-et-Marne et du Val d'Oise
departements = [["75 - Paris", "https://www.adresses-mairies.fr/departement-paris-76.html"]]

# Pour avoir des Excel unique à chaque fois, avec sa date et heure de génération
now = datetime.now()
date = now.strftime("%d-%m-%Y_%Hh%M")
workbook = xlsxwriter.Workbook("scraping_" + date + ".xlsx")

# Formatting de l'Excel
bold = workbook.add_format({'bold': True})

# Pour chaque département, on va chercher chacune des villes
for departement in departements :
    # On crée une feuille Excel par département
    worksheet = workbook.add_worksheet(departement[0])

    worksheet.write('A1', 'Ville', bold)
    worksheet.write('B1', 'Téléphone', bold)
    worksheet.write('C1', 'E-mail', bold)

    row = 1

    response = requests.get(departement[1])
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    # Récupérer la liste des villes du département
    for ultag in soup.find_all('ul', {'class': 'liste_mairie2'}):     
        for litag in ultag.find_all('li'):
            ville_url = litag.a.get('href')

            # Requêter chaque ville
            response2 = requests.get("https://www.adresses-mairies.fr" + ville_url)
            html2 = response2.content
            soup2 = BeautifulSoup(html2, 'html.parser', from_encoding="utf-8")

            # Récupérer le nom de la ville
            name = soup2.find('h1').text.replace("Mairie de ", "").replace("Mairie d'", "")

            # Récupérer la balise coordonnees comportant n° + mail de la ville
            phone = "/"
            mail = "/"
            for ultag2 in soup2.find_all('ul', {'class': 'coordonnees'}):
                for litag2 in ultag2.find_all('li'):
                    phone_regex = re.search('(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})', litag2.text)
                    if phone_regex :
                        phone = phone_regex.group(0)

                    mail_regex = re.search('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', litag2.text)
                    if mail_regex :
                        mail = mail_regex.group(0)

            # Check
            print(name + "  " + phone + "  " + mail)

            # On écrit dans le fichier les informations
            worksheet.write(row, 0, name)
            worksheet.write(row, 1, phone)
            worksheet.write(row, 2, mail)

            row += 1

workbook.close()
