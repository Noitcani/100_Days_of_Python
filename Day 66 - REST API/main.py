from flask import Flask, jsonify, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dict_output = {}
        for col in self.__table__.columns:
            dict_output[col.name] = getattr(self, col.name)
        return dict_output


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    return jsonify(random_cafe.to_dict())


@app.route("/all")
def get_all():
    cafe_list = []
    all_cafes = Cafe.query.all()
    for cafe in all_cafes:
        cafe_list.append(cafe.to_dict())
    return jsonify(cafe_list)


@app.route('/search', methods=["GET"])
def search():
    location_to_search = request.args["loc"]
    search_results = Cafe.query.filter_by(location=location_to_search).all()
    if search_results != []:
        found_list = [cafe.to_dict() for cafe in search_results]
        return jsonify(found_list)

    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route('/addcafe', methods=["POST"])
def add():
    form_details = request.form.to_dict()
    for key, value in form_details.items():
        if value.title() == "True":
            form_details[key] = True
        elif value.title() == "False":
            form_details[key] = False

    new_cafe = (Cafe(**form_details))
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Cafe added successfully"})


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update == None:
        return jsonify(error={"Not Found": "Sorry, cafe with that ID is not found in DB."}), 404
    else:
        cafe_to_update.coffee_price = request.args['new_coffee_price']
        db.session.commit()
        return jsonify({"Success": "Successfully updated price"})


@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    api_key = request.args['api_key']
    if api_key == "topsecretkey":
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        if cafe_to_delete == None:
            return jsonify(error={"Not Found": "Sorry, cafe with that ID is not found in DB."}), 404
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({"Success": f'Successfully deleted cafe with id {cafe_id}'})
    else:
        return jsonify(error={"Not Authorized": "You do not seem to have the correct api_key"}), 403


if __name__ == '__main__':
    app.run(debug=True)
