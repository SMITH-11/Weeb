from flask import Blueprint, render_template, request
from trending import get_trending_data
from search import searchAnime
from detail import get_anime_details
import random

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def home():
    return render_template('home.html')

@routes.route('/search', methods=['GET', 'POST'])
def search():
    name = request.form['myform']
    data = searchAnime(name)
    return render_template('search.html', data=data, title=name)


@routes.route('/trending')
def trending():
    trending_data = get_trending_data()
    return render_template('trending.html', data=trending_data)

@routes.route('/anime/<int:mal_id>')
def know_more(mal_id):
    data = get_anime_details(mal_id)
    image = data['image_url']
    print(image)
    return render_template('know_more.html', data=data, img=image)