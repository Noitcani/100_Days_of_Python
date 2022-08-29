from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired, NumberRange
import os

app = Flask(__name__)
app.secret_key = "12345"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'books-collection.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


class edit_rating(FlaskForm):
    new_rating = FloatField(label="New Rating", validators=[
                            DataRequired(), NumberRange(min=0, max=10)])


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    all_books = Books.query.all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        booktitle = request.form['title']
        bookauthor = request.form['author']
        bookrating = request.form['rating']
        entry = Books(title=booktitle, author=bookauthor, rating=bookrating)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('add.html')


@app.route("/edit/<book_title>", methods=["GET", "POST"])
def edit(book_title):
    edit_rating_form = edit_rating()
    edit_rating_form.validate_on_submit()
    book_to_update = Books.query.filter_by(title=book_title).first()
    if edit_rating_form.validate_on_submit() and request.method == "POST":
        book_to_update.rating = edit_rating_form.new_rating.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', edit_rating_form=edit_rating_form, book_to_update=book_to_update)


@app.route("/delete/<book_title>", methods=["GET", "POST"])
def delete(book_title):
    book_to_delete = Books.query.filter_by(title=book_title).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
