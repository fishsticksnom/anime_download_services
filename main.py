import os
from pprint import pprint
from modules.get_episodes import get_episodes
from modules.get_file_source import get_file_source

ANIME_URL = os.environ.get("ANIME_URL")

url = f"{ANIME_URL}/tokyo-ghoul-castellano-sub-espanol"

anime_episodes = get_episodes(url)

downloads = []
episode_number = 1

for episode in anime_episodes:
    episode_and_services = {
        "episode": episode_number,
        "services": get_file_source(episode),
    }
    downloads.append(episode_and_services)
    episode_number = episode_number + 1

pprint(downloads)
