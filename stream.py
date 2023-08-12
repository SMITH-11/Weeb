import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def remove_ads(soup):
    # Find and remove ad-related elements based on their classes, IDs, attributes, etc.
    ad_classes = ["ad-class", "another-ad-class"]
    ad_ids = ["ad-id", "another-ad-id"]
    
    for ad_class in ad_classes:
        for ad in soup.find_all(class_=ad_class):
            ad.decompose()  # Remove the ad element
    
    for ad_id in ad_ids:
        ad = soup.find(id=ad_id)
        if ad:
            ad.decompose()  # Remove the ad element

    # More ad removal logic can be added here
    
    return soup

def get_stream_url(title):
    name = quote(title.replace(" ", '-').replace("(", '').replace(")", '').replace(":", ''))
    base_url = f"https://www4.gogoanimes.fi/{name}-episode-1"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove ads from the soup object
        cleaned_soup = remove_ads(soup)
        
        ep_link = cleaned_soup.find('iframe')['src']
        return ep_link
    else:
        return None
