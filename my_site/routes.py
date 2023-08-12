from flask import Blueprint, render_template, flash, redirect, url_for
from home import get_home_data
from detail import scrape_category_details  # Make sure to provide the correct import path
from stream import get_stream_url

routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def home():
    data = get_home_data(pages=2)
    return render_template('home.html', data=data)

@routes.route('/category/<title>')
def category(title):
    anime_data = scrape_category_details(title)
    if anime_data:
        return render_template('detail.html', anime_data=anime_data)
    else:
        flash("An error occurred while fetching data from the category page.")
        return redirect(url_for('routes.home'))

@routes.route('/stream/<title>')
def stream(title):
    stream_url = get_stream_url(title)
    
    if stream_url:
        return render_template('stream.html', stream_url=stream_url, title=title)
    else:
        flash("An error occurred while fetching the stream URL.")
        return redirect(url_for('routes.home'))