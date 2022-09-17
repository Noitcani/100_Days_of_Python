from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreateLoginForm, CreatePostForm, CreateRegisterForm, CreateCommentForm
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLES

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    authored_posts = relationship(
        "BlogPost", back_populates='author', lazy=True)
    authored_comments = relationship(
        "Comments", back_populates='author', lazy=True)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship(
        "User", back_populates='authored_posts', lazy=True)
    comments = relationship(
        "Comments", back_populates='blogpost', lazy=True)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = relationship(
        "User", back_populates='authored_comments', lazy=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    blogpost = relationship(
        "BlogPost", back_populates='comments', lazy=True)
    blogpost_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'))


db.create_all()


def admin_only(f):
    @wraps(f)
    def wrapper_func(*args, **kwargs):
        if (not current_user.is_anonymous) and (current_user.is_admin):
            return f(*args, **kwargs)
        else:
            return abort(403)
    return wrapper_func


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/<author_name>')
def get_all_posts_by_author(author_name):
    user = User.query.filter_by(name=author_name).first()
    user_posts = user.authored_posts
    return render_template("index.html", all_posts=user_posts)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = CreateRegisterForm()
    if form.validate_on_submit():
        new_user = User(
            email=request.form['email'],
            password=generate_password_hash(
                request.form['password'], method='pbkdf2:sha256', salt_length=8),
            name=request.form['name'],
            is_admin=False
        )
        if User.query.filter_by(email=new_user.email).first():
            flash('Email already registered.')
            return render_template("register.html", form=form)

        else:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = CreateLoginForm()
    if form.validate_on_submit():
        trying_user = User.query.filter_by(email=request.form['email']).first()
        if (trying_user != None) and (check_password_hash(trying_user.password, request.form['password'])):
            login_user(trying_user)
            return redirect(url_for('get_all_posts'))
        else:
            flash('Login failed. Either email or password entered is invalid.')
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    form = CreateCommentForm()
    if form.validate_on_submit():
        if not current_user.is_anonymous:
            comment = Comments(date=date.today().strftime(
                "%B %d, %Y"), body=form.comment_body.data, author=current_user, blogpost=requested_post)
            db.session.add(comment)
            db.session.commit()
            return render_template("post.html", post=requested_post, form=form)
        else:
            flash('Please login to post comment!')
            return redirect(url_for('login'))
    return render_template("post.html", post=requested_post, form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = post.author
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
