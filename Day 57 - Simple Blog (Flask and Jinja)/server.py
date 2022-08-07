from flask import Flask, render_template
import datetime as dt
from requests_html import HTMLSession

app = Flask(__name__)

current_year = dt.datetime.now().year
my_name = "Noitcani"
AGEIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"
BLOG_CONTENT_URL = "https://api.npoint.io/c790b4d5cab58020d391"

blog_session = HTMLSession()
blog_data = blog_session.get(BLOG_CONTENT_URL).json()


@app.route("/")
def serve_homepage():
    return render_template("index.html", blog_data=blog_data)


@app.route("/guess/<nameinput>")
def serve_guesspage(nameinput):
    ageify_session = HTMLSession()
    ageify_params = {
        "name": nameinput,
    }
    ageify_response = ageify_session.get(url=AGEIFY_URL, params=ageify_params)
    predicted_age = ageify_response.json()["age"]

    genderize_session = HTMLSession()
    genderize_params = {
        "name": nameinput,
    }
    genderize_response = genderize_session.get(
        url=GENDERIZE_URL, params=genderize_params)
    predicted_gender = genderize_response.json()["gender"]
    gender_confidence = (genderize_response.json()["probability"] * 100)

    # return (predicted_age, predicted_gender)
    return render_template("age_gender.html", nameinput=nameinput.title(), age_output=predicted_age, gender_output=predicted_gender, prob_output=gender_confidence)


@app.route("/post/<int:postid>")
def serve_post(postid):
    return render_template("post.html", blog_data=blog_data, postid=postid)


if __name__ == "__main__":
    app.run(debug=True)
