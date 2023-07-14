import requests
def get_anime_details(mal_id):
    url = f"https://api.jikan.moe/v4/anime/{mal_id}"
    response = requests.get(url)
    data = response.json()["data"]
    
    mal_id = data["mal_id"]
    url = data["url"]
    image_url = data["images"]["webp"]["image_url"]
    trailer_embed_url = data["trailer"]["embed_url"]
    titles = [title["title"] for title in data["titles"]]
    title = data['title']
    name_eng =data["title_english"]
    name_jap = data["title_japanese"]
    title_synonyms = data["title_synonyms"]
    anime_type = data["type"]
    source = data["source"]
    episodes = data["episodes"]
    status = data["status"]
    aired_from = data["aired"]["from"]
    aired_to = data["aired"]["to"]
    aired_string = data["aired"]["string"]
    duration = data["duration"]
    rating = data["rating"]
    score = data["score"]
    scored_by = data["scored_by"]
    rank = data["rank"]
    synopsis = data["synopsis"]
    background = data["background"]
    season = data["season"]
    year = data["year"]
    broadcast_day = data["broadcast"]["day"]
    broadcast_time = data["broadcast"]["time"]
    broadcast_timezone = data["broadcast"]["timezone"]
    broadcast_string = data["broadcast"]["string"]
    producers = [{"name": producer["name"], "url": producer["url"]} for producer in data["producers"]]
    licensors = [{"name": licensor["name"], "url": licensor["url"]} for licensor in data["licensors"]]
    studios = [{"name": studio["name"], "url": studio["url"]} for studio in data["studios"]]
    genres = [{"name": genre["name"], "url": genre["url"]} for genre in data["genres"]]
    themes = [{"name": theme["name"], "url": theme["url"]} for theme in data["themes"]]
    demographics = [{"name": demographic["name"], "url": demographic["url"]} for demographic in data["demographics"]]
    
    anime_details = {
        "mal_id": mal_id,
        "url": url,
        "image_url": image_url,
        "trailer_embed_url": trailer_embed_url,
        "titles": titles,
        "title": title,
        "nameJap": name_jap,
        "nameEng": name_eng,
        "title_synonyms": title_synonyms,
        "type": anime_type,
        "source": source,
        "episodes": episodes,
        "status": status,
        "aired_from": aired_from,
        "aired_to": aired_to,
        "aired_string": aired_string,
        "duration": duration,
        "rating": rating,
        "score": score,
        "scored_by": scored_by,
        "rank": rank,
        "synopsis": synopsis,
        "background": background,
        "season": season,
        "year": year,
        "broadcast_day": broadcast_day,
        "broadcast_time": broadcast_time,
        "broadcast_timezone": broadcast_timezone,
        "broadcast_string": broadcast_string,
        "producers": producers,
        "licensors": licensors,
        "studios": studios,
        "genres": genres,
        "themes": themes,
        "demographics": demographics
    }
    
    return anime_details