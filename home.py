import requests
from bs4 import BeautifulSoup
import json

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        anime_items = soup.select(".last_episodes > ul.items > li")
        data = []

        for anime_item in anime_items:
            title = anime_item.select_one(".name a")["title"]
            image_link = anime_item.select_one("img")["src"]
            
            # Extract the modified card_link
            card_link = image_link.replace("https://gogocdn.net/cover/", "").replace('.png', '')
            card_link = image_link.replace("https://gogocdn.net/images/anime/N/", "").replace('.png', '').replace('.jpg', '')
            # print(card_link)
            if card_link.rsplit('-', 1)[-1].isnumeric():
                card_link = card_link.rsplit('-', 1)[0]  # Removed the ".pop"
            # print(card_link)
            
            
            anime_data = {"title": title, "image": image_link, "card_link": card_link}
            data.append(anime_data)

        return data
    else:
        return None

def get_home_data(pages=10):
    base_url = "https://www4.gogoanimes.fi/?page="
    all_data = []

    for page_number in range(1, pages + 1):
        page_url = base_url + str(page_number)
        data = scrape_page(page_url)
        all_data.extend(data)

    return all_data

if __name__ == '__main__':
    data = get_home_data(pages=1)

