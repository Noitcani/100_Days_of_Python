from flask import Flask, render_template
from requests_html import HTMLSession
import json

# session = HTMLSession()

# res = session.get("https://api.npoint.io/c790b4d5cab58020d391")
# with open("blog_data.json", "w", encoding="utf-8") as f:
#     f.write(res.text)

app = Flask(__name__)


with open("blog_data.json", "r") as f:
    blogdata = json.load(f)


@app.route("/")
def serve_homepage():
    return render_template("index.html", blogdata=blogdata)


@app.route("/about")
def serve_aboutpage():
    return render_template("about.html")


@app.route("/contact")
def serve_contactpage():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def serve_post(post_id):
    return render_template("post.html", blogdata=blogdata, post_id=post_id)


if __name__ == "__main__":
    app.run(debug=True)
