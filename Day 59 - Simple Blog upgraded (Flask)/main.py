from flask import Flask, render_template, request
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


@app.route("/contact", methods=["POST", "GET"])
def serve_contactpage():
    if request.method == "POST":
        email_content = {
            "user_name": request.form['name'],
            "user_email": request.form['email'],
            "user_phone": request.form['phonenumber'],
            "user_message": request.form['message'],
        }
        successful_message = 'Successfully Submitted Your Message!'
        with open("email_to_send.json", "w") as f:
            json.dump(email_content, f, indent=4)

        return render_template("contact.html", successful_message=successful_message)

    elif request.method == "GET":
        return render_template("contact.html", successful_message="")


@app.route("/post/<int:post_id>")
def serve_post(post_id):
    return render_template("post.html", blogdata=blogdata, post_id=post_id)


# @app.route("/form-entry", methods=["POST"])
# def form_entry():


if __name__ == "__main__":
    app.run(debug=True)
