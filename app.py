from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROPERTIES = [
  {
    'room_no': 501,
    'title': '1BHK',
    'location': 'Dublin, Ireland',
    'price': '$50000'
  },
  {
    'room_no': 502,
    'title': '1.5BHK',
    'location': 'Dublin, Ireland',
    'price': '$70000'
  },
  {
    'room_no': 605,
    'title': '3BHK',
    'location': 'Dublin, Ireland',
    'price': '$90000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', properties=PROPERTIES)


@app.route("/api/properties")
def list_properies():
  return jsonify(PROPERTIES)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
