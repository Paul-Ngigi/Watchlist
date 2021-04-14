from flask import render_template
from app import app
from .request import get_movies, get_movie, search_movie


# Views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    # Getting popular movie
    popular_movie = get_movies('popular')
    print(popular_movie)

    # Getting upcoming movie
    upcoming_movie = get_movies('upcoming')
    print(upcoming_movie)

    # Getting now playing
    now_showing_movie = get_movies('now_playing')
    print(now_showing_movie)
    title = 'Home - Welcome to The Best Movie Review Website Online'
    return render_template('index.html', title=title, popular=popular_movie, upcoming=upcoming_movie,
                           now_showing=now_showing_movie)


@app.route('/movie/<int:id>')
def movie(id):
    """
    View movie page function that returns the movie details page and its data
    """
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title=title, movie=movie)


@app.route('/search/<movie-name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)