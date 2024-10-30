import requests
from bs4 import BeautifulSoup

URL = "https://www.vinted.fr/vetements?search_text=veste+nike"  # Remplace par l'URL Vinted que tu veux surveiller

def check_vinted():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("div", class_="FeedItem__content")

    if items:
        print("Nouveaux articles trouvés sur Vinted!")
    else:
        print("Aucun nouvel article.")

if __name__ == "__main__":
    check_vinted()
