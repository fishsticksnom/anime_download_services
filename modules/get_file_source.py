import requests
from bs4 import BeautifulSoup


def get_file_source(episode_link):
    request = requests.get(episode_link)
    episode_content = BeautifulSoup(request.content, "html.parser")
    download_sources = episode_content.find_all("a", {"aria-label": "Boton descargar"})
    download_links = []
    for a in download_sources:
        download_links.append(a["href"])

    return download_links
