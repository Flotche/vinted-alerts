import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

URL = "https://www.vinted.fr/vetements?search_text=veste+nike"  # Remplace par l'URL Vinted que tu veux surveiller
EMAIL = os.getenv("EMAIL")  # Récupérer l'email à partir des secrets
PASSWORD = os.getenv("PASSWORD")  # Récupérer le mot de passe à partir des secrets

def send_email():
    subject = "Nouveaux articles trouvés sur Vinted"
    body = "Il y a de nouveaux articles sur la page Vinted que tu surveilles!"
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, EMAIL, msg.as_string())
        server.quit()
        print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

def check_vinted():
    try:
        response = requests.get(URL)
        print(f"Statut de la réponse HTTP : {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            items = soup.find_all("div", class_="FeedItem__content")
            print(f"Nombre d'articles trouvés : {len(items)}")

            if len(items) > 0:
                print("Nouveaux articles trouvés.")
                send_email()
            else:
                print("Aucun nouvel article trouvé.")
        else:
            print("Erreur lors de la requête HTTP.")
    except Exception as e:
        print(f"Erreur lors de la récupération des données : {e}")

if __name__ == "__main__":
    check_vinted()
