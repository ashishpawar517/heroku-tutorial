import requests
from bs4 import BeautifulSoup
import random
from tabulate import tabulate

total_seasons = 12
max_ep = 24


def scrape():
    r1 = random.randint(1, total_seasons)
    r2 = random.randint(1, max_ep)

    base_url = "https://the-big-bang-theory.com/quotes/episode/"

    complete_url = base_url + str(r1) + str(r2) + str("")

    out = requests.get(complete_url)
    # out = requests.get(base_url+str('822'))

    # print(out.text)
    soup = BeautifulSoup(out.content, "html.parser")
    
    quotes = soup.findAll("div", class_="quotesBody")
    name = soup.findAll("td", class_="cltbtdh")
    return quotes,name

def get():

    quotes,name = [], []
    while len(quotes) == 0 and len(name) == 0:
        quotes,name = scrape()

    id, epname, date = name[0].get_text().split("\n")[5:8]
    r3 = random.randint(1, len(quotes))

    data = [["The Big Bang Theory, "+id + "\n" +epname.replace("-", "", 1)], [quotes[r3].get_text()]]

    return tabulate(data, tablefmt="html")
