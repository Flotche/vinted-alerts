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

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, EMAIL, msg.as_string())
    server.quit()

def check_vinted():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("div", class_="FeedItem__content")

    if items:
        send_email()

if __name__ == "__main__":
    check_vinted()
