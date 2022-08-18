from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def serve_homepage():
    return render_template("index.html")


@app.route("/login", methods=['post'])
def serve_login():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        return render_template("login.html", USERNAME=user, PASSWORD=password)


if __name__ == "__main__":
    app.run(debug=True)
