import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_wikipedia_table(url: str, table_index: int = 0):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    df = pd.read_html(str(tables[table_index]))[0]
    return df