import requests
from bs4 import BeautifulSoup
import json

def scrape(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any request errors
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find('ul', class_="items")
        data_list = []  # List to store information about all the items

        for li in items.find_all('li'):
            data = {}  # Create a new dictionary for each item
            image_div = li.find('div', class_="img")
            images = image_div.find('img')['src']
            data.update({"image": images})
            title = li.find('p', class_="name").text
            data.update({"title": title})
            data_list.append(data)  # Add the current item's data to the list

        return json.dumps(data_list)  # Return the list of items as JSON string
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return "[]"

def get_popular_data(total_pages=1):
    all_data = []
    base_url = "https://www4.gogoanimes.fi/popular.html"
    for i in range(1, total_pages + 1):
        url = f"{base_url}?page={i}"
        print(f"Scraping data from page {i}")
        data = scrape(url)
        all_data.extend(json.loads(data))  # Append the data from each page to the list
    return all_data

if __name__ == "__main__":
    all_data_json = get_popular_data(3)
    print(all_data_json)