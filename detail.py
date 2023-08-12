import requests
from bs4 import BeautifulSoup

def scrape_category_details(title):
    # title_formatted = title.replace("-", " ").title()
    url = f"https://www4.gogoanimes.fi/category/{title}"
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        anime_detail = soup.find("div", class_="anime_info_body_bg")

        img = anime_detail.find("img")["src"]
        anime_name = anime_detail.find("h1").text

        anime_details = anime_detail.find_all("p")
        Name = anime_details[1].find("a").text
        Plot = anime_details[2].text.replace("Plot Summary: ", "")
        Genre = anime_details[3].find("a").text
        Released = anime_details[4].text.replace("Released: ", "")
        Status = anime_details[5].find("a").text
        Other_Name = anime_details[6].text.replace("Other name: ", "")

        anime_data = {
            "img": img,
            "anime_name": anime_name,
            "Name": Name,
            "Plot": Plot,
            "Genre": Genre,
            "Released": Released,
            "Status": Status,
            "Other_Name": Other_Name
        }

        return anime_data
    else:
        return None
