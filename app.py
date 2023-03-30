from flask import Flask  #Flask class
from flask import render_template  #to render all templates
from flask import jsonify # To convert dictionary text to json

app = Flask(__name__)  # define class

pekerjaan = [{
  'id': 1,
  'title': 'Data Scientist',
  'salary': 'Rs. 15,000,000'
}, {
  'id': 2,
  'title': 'Data Engineer',
  'location': 'Singapore',
}, {
  'id': 3,
  'title': 'Business Analyst',
  'location': 'Indonesia',
  'salary': 'Rp. 15,000,000'
}]


@app.route("/") # don't add any new url
def hello_world():
  return render_template(
    'home.html', job=pekerjaan, company_name="PAKO"
  )  #jobs is going to make JOBS dictionary can be access in html file -- showing dynamic data

@app.route("/job") # add "/job" url to access dictionary data (json format -- restAPI)
def list_jobs():
  return jsonify(pekerjaan)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
