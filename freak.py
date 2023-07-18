import requests
from bs4 import BeautifulSoup
import re


def get_episode_num(verified, url):
    response = requests.get(verified)
    soup = BeautifulSoup(response.content, 'html.parser')
    num = soup.find_all('div', class_="item-title")
    if len(num) >= 4:
        episode_number = num[3].text.split(" ")[-1]
    else:
        gogourl = "https://www4.gogoanimes.fi/search.html?keyword=" + url
        response = requests.get(gogourl)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.select("ul.items > li > p.name > a")
        #print(data)
        if data:
            episode_url = "https://www4.gogoanimes.fi" + data[0].get("href")
            #print(episode_url)
            episode_response = requests.get(episode_url)
            episode_soup = BeautifulSoup(episode_response.content, 'html.parser')
            episode_element = episode_soup.select_one("ul#episode_page li a.active")
            if episode_element:
                episode_number = episode_element.get("ep_end")
            else:
                episode_number = 5
            #print(episode_number)
        else:
            episode_number = 5
    #print(episode_number)
    return episode_number






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
    #print(verified_url)
    #print(url)
    episode_num = int(get_episode_num(verified_url, url))
    #print(episode_num)
    episode_urls = get_episode(url, episode_num)
    return episode_urls, episode_num

# get_episode_num("https://animefreak.site/anime/zom-100-zombie-ni-naru-made-ni-shitai-100-no-koto")