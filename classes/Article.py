from datetime import date
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Article:
    def __init__(self, url):
        self.url = url
        self.date = date.today()
        self.journal = self.get_domain()
        self.content = self.get_text()

    def get_domain(self):
        parsed_url = urlparse(self.url)
        domain = '{uri.netloc}'.format(uri=parsed_url).replace("www.", "")
        return domain

    def get_text(self):
        url = self.url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Grap_title
        title = soup.find_all(class_='c-title')
        # remove undesired tags

        # Grap content
        content = soup.find_all(class_='c-body'):
        # remove undesired tags


Article("https://www.francetvinfo.fr/economie/crise/blocus-des-agriculteurs/colere-des-agriculteurs-la-principale-cause-de-cette-crise-est-le-non-respect-de-la-loi-egalim-par-les-distributeurs-deplore-une-federation-de-l-agroalimentaire_6326988.html")
