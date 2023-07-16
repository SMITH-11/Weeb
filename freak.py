import requests
from bs4 import BeautifulSoup
import re


def get_episode_num(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    num = soup.find_all('div', class_="item-title")
    print(num[3].text.split(" ")[-1])
    return (num[3].text.split(" ")[-1])


def verify(url):
    merged_url = re.sub(r'[-_]+', '-', url)
    # get_episode(merged_url, episodes)
    return merged_url

def get_title(name):
    urlvalue = name.replace(':', "").replace(' ', '-').replace('.','')
    #verify(urlvalue)
    return urlvalue


def get_episode(japurl, episodes):
    urls = []
    for i in range(1, episodes + 1):
        base_url = f"https://9anime.skin/stream/play.php?slug={japurl}"#-episode-{i}
        urls.append(base_url)
        # print(urls)
    return urls

def main(title):     
    japname = get_title(title)
    verified_url = "https://animefreak.site/anime/"+ verify(japname)
    url = verify(japname)
    print(verified_url)
    print(url)
    episode_num = int(get_episode_num(verified_url))
    print(episode_num)
    episode_urls = get_episode(url, episode_num)
    return episode_urls, episode_num

# get_episode_num("https://animefreak.site/anime/zom-100-zombie-ni-naru-made-ni-shitai-100-no-koto")