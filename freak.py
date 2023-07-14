# import requests
# import bs4
import re

def verify(url, episodes):
    merged_url = re.sub(r'[-_]+', '-', url)
    get_episode(merged_url, episodes)
    return merged_url




def get_title(name):
    urlvalue = name.replace(':', "").replace(' ', '-').replace('.','')
    #verify(urlvalue)
    return urlvalue


def get_episode(japurl, episodes):
    urls = []
    if episodes == 'undefined':
        return urls.append[-1]
    for i in range(1, episodes + 1):
        base_url = f"https://9anime.skin/stream/play.php?slug={japurl}-episode-{i}"
        urls.append(base_url)
        # print(urls)
    return urls


def main(title, episodes):     
    japname = get_title(title)
    verified_url = verify(japname, episodes)
    episode_urls = get_episode(verified_url, episodes)
    return episode_urls
