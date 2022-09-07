from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DOWNLOAD_FOLDER'] = 'static/files'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user_info = {}
        new_user_info['name'] = request.form['name']
        new_user_info['email'] = request.form['email']
        new_user_info['password'] = generate_password_hash(
            request.form['password'], 'pbkdf2:sha256', 8)

        if db.session.query(User).filter_by(email=new_user_info['email']).first():
            flash('Email already registered!')
            return redirect(url_for('home'))

        new_user = User(**new_user_info)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets', user=new_user.name))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = db.session.query(User).filter_by(email=email).first()
        if user != None:
            if check_password_hash(user.password, password):
                login_user(user)
                flash(f'Welcome {user.name}. Logged in successfully.')
                return render_template("secrets.html", user=user.name)
            else:
                flash('Incorrect password')
        else:
            flash('No such user')
    return render_template("login.html")


@app.route('/secrets/<user>')
@login_required
def secrets(user):
    return render_template("secrets.html", user=user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], 'cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
