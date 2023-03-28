from flask import Flask  #Flask class
from flask import render_template  #to render all templates

app = Flask(__name__)  # define class

pekerjaan = [{
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,000,000'
}, {
  'id': 2,
  'title': 'Data Engineer',
  'location': 'Singapore',
  'salary': '$.15,000'
}, {
  'id': 3,
  'title': 'Business Analyst',
  'location': 'Indonesia',
  'salary': 'Rp. 15,000,000'
}]


@app.route("/")
def hello_world():
  return render_template(
    'home.html', job=pekerjaan
  )  #jobs is going to make JOBS dictionary can be access in html file -- showing dynamic data


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
