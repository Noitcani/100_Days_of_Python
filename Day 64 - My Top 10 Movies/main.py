from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from requests_html import HTMLSession
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
load_dotenv()

# SQLAlchemy Setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'moviesdb.db')

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(300), nullable=False)


db.create_all()

# Flask Forms


class RateMovieForm(FlaskForm):
    rating_field = FloatField(label="Rating", validators=[
        DataRequired(), NumberRange(min=0, max=10, message="Please key in a valid value")])
    review_field = StringField(
        label="Review", validators=[DataRequired(message="Please key in a review")])

    submit_field = SubmitField(label="Update")


class AddMovieForm(FlaskForm):
    new_movie_field = StringField(label="Add Movie", validators=[
        DataRequired(message="Please type in a Movie name to add")])
    submit_field = SubmitField(label="Add")


# MovieDB API
session = HTMLSession()
MOVIEDB_APIKEY = os.environ["MOVIEDB_APIKEY"]
MOVIEDB_BEARER = os.environ["MOVIEDB_BEARER"]


def find_movie_id(movie_title):
    end_pt = 'https://api.themoviedb.org/3/search/movie?'
    headers = {
        # 'api_key': MOVIEDB_APIKEY,
        'Authorization': f'Bearer {MOVIEDB_BEARER}',
        'Content-Type': 'application/json;charset=utf-8',
    }
    params = {
        'query': movie_title,
    }
    movie_info = session.request(
        method="GET", url=end_pt, params=params, headers=headers)
    return movie_info


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    i = 1
    for movie in all_movies:
        movie.ranking = i
        i += 1
    db.session.commit()
    all_movies = all_movies[:10]
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    all_movies = Movie.query.all()
    form = RateMovieForm()
    if form.validate_on_submit():
        all_movies = Movie.query.all()
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = form.rating_field.data
        movie_to_update.review = form.review_field.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", all_movies=all_movies, movie_id=movie_id, form=form)


@app.route('/delete/<int:movie_id>', methods=["GET", "POST"])
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_to_add = form.new_movie_field.data
        searched_info = find_movie_id(movie_to_add).json()
        with open("temp.json", "w") as f:
            json.dump(searched_info, f, indent=4)
        searched_movies_list = searched_info['results']
        return render_template('select.html', searched_movies_list=searched_movies_list)

    return render_template('add.html', form=form)


@app.route('/add_to_home/<int:movie_id>')
def add_movie_to_home(movie_id):
    with open("temp.json", "r") as f:
        searched_movies_list = json.load(f)['results']

    for movie in searched_movies_list:
        if movie['id'] == movie_id:
            movie_to_add = Movie(title=movie["title"], year=movie["release_date"].split('-')[0], description=movie["overview"],
                                 rating=0, ranking=0, review="Pending", img_url=f'https://image.tmdb.org/t/p/w200/{movie["poster_path"]}')
            db.session.add(movie_to_add)
            db.session.commit()
            return redirect(url_for('edit', movie_id=movie_to_add.id))


if __name__ == '__main__':
    app.run(debug=True)
