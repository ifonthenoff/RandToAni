import requests
from enum import Enum
from bs4 import BeautifulSoup

class Anime:
    def __init__(self, title: str, episodesWatched: int, score: str, url: str):
        self.title = title
        self.episodesWatched = episodesWatched
        self.score = score
        self.url = url

class Status(Enum):
    comp = "COMPLETED"
    curr = "CURRENT"
    plan = "PLANNING"
    drop = "DROPPED"
    hold = "PAUSED"

def crawlList(url: str, types: list) -> dict:
    doc = BeautifulSoup(requests.get(url).text, "html.parser")
    rs = doc.select_one(".general").find_all("table", {"data-id":types})
    animes = dict()

    for result in rs:
        type = types.pop(0)

        subrs = result.select_one("tbody").select("tr")
        animes[type] = list()

        for anime in subrs:
            title = anime.select("td")[0].select_one("a").text.strip()
            episodes = int(anime.select("td")[1].select_one("span").get("data-progress")[:-2].strip())
            score = anime.select("td")[4].select_one("div").select_one("div").text.strip()

            url = anime.select_one("td").select_one("a").get("href")
            if not score: score = None

            animes[type].append(Anime(title, episodes, score, url))

    return animes

def getAlternateNames(url: str) -> list:
    rs = BeautifulSoup(requests.get(url).text, "html.parser").find("div", {"itemprop": "alternateName"})
    if not rs:
        return None
    else:
        return [name.replace(" ", "").strip().upper() for name in rs.text.split(",")]

def getUsername():
    headers = {'User-Agent': 'Chrome/81.0.4044.138',
               "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
    payload = {"username": "Chancentod", "ratoken": "4fcbbf5b247e513519a1b2c9809262b6", "submit": "Suchen"}
    add_cookies = {"_ga": "GA1.2.636808033.1580845866",
                   "ra_ra_app_token": "69b3d1b54aa18b0595892efb67571072ea8e6a5c.754673a4995aed862f3cb4b39c2be9879919c32b57afbf657211c55595c6753563caa1f4061c9cfa1a724a87ccd8701277f38cadecd0d3ffdee21b274bcb7c1c"}
    link = "https://randaris.app/userlist"

    session = requests.Session()

    resp = session.get(link)
    # print(resp.headers)
    cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))

    requests.utils.add_dict_to_cookiejar(cookies, add_cookies)

    resp = session.post(link, headers=headers, data=payload, cookies=cookies)
    print(cookies)
    print(resp.status_code)
