import requests

def get_trending_data():
  url = "https://api.jikan.moe/v4/top/anime"
  response = requests.get(url)
  data = response.json()
  anime_list = data["data"]

  mal_id = []
  thumbnail = []
  name_eng = []
  name_jap = []
  name_syn = []
  Type = []
  duration = []
  source = []
  episodes = []
  status = []
  score = []
  season = []
  year = []
  description = []
  genres = []
  trailer_embed_url = []

  for anime in anime_list:
    mal_id.append(anime["mal_id"])
    image = anime["images"]["webp"]["image_url"]
    thumbnail.append(image)
    name_eng.append(anime["title_english"])
    name_jap.append(anime["title_japanese"])
    name_syn.append(anime.get("title_synonyms", []))
    Type.append(anime["type"])
    duration.append(anime["duration"])
    source.append(anime["source"])
    episodes.append(anime["episodes"])
    status.append(anime["status"])
    score.append(anime["score"])
    season.append(anime["season"])
    year.append(anime["year"])
    description.append(anime["synopsis"])
    genres_data = anime["genres"]
    genres_list = [genre["name"] for genre in genres_data]
    genres.append(genres_list)
    trailer_embed_url.append(anime["trailer"]["embed_url"])

  return {
    "mal_id": mal_id,
    "thumbnail": thumbnail,
    "nameEng": name_eng,
    "nameJap": name_jap,
    "name_syn": name_syn,
    "type": Type,
    "duration":duration,
    "source": source,
    "episodes": episodes,
    "status": status,
    "score": score,
    "season": season,
    "year": year,
    "description": description,
    "genres": genres,
    "trailer_embed_url": trailer_embed_url
  }
