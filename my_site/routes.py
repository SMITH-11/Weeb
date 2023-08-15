from flask import Blueprint, render_template, flash, redirect, url_for, request
from home import get_home_data
from detail import scrape_category_details  # Make sure to provide the correct import path
from search import get_search_data
from stream import get_stream_url
from trending import get_popular_data

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
    
@routes.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        anime_name = request.form.get("myform")
        anime_data = get_search_data(anime_name)
        return render_template("search.html", data=anime_data)  # Use your existing template
    return redirect(url_for("routes.home"))  # Redirect to home if GET request

@routes.route("/trending")
def trending():
    data=get_popular_data(1)
    # print(data)
    return render_template("trending.html",data=data)
