import requests
from bs4 import BeautifulSoup


def get_episodes(url):
    request = requests.get(url)
    website_content = BeautifulSoup(request.content, "html.parser")
    div_episodes = website_content.find_all("div", {"class", "col-item"})

    link_episodes = []

    for div in div_episodes:
        link_episodes.append(div.a["href"])

    return link_episodes
