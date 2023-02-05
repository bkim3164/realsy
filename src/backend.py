from flask import Flask, jsonify, request
import json
import os
import psycopg2


# Create a Flask server.
app = Flask(__name__)

# Create a cursor and initialize psycopg
db_url = 'postgresql://brian:rtsNRr0uzXSWexZupx9wxw@forest-grizzly-4869.6wr.cockroachlabs.cloud:26257/forest-grizzly-4869.defaultdb?sslmode=verify-full'

connection = psycopg2.connect(db_url)
cursor = connection.cursor()


def fetch_data():
    cursor.execute("SELECT * FROM agent WHERE location= ")
    results = cursor.fetchall()
    return results

@app.route('/get-location', methods=['POST']) 
def get_(): # handle the POST request 
    if request.method == 'POST': 
        location = request.form.get('location')
        # ...
        # 
        return {
            "Hello": "World"
        } 
@app.route('/get-location', methods=['POST']) 
def get_(): # handle the POST request 
    if request.method == 'POST': 
        location = request.form.get('location')

        # ...
        # 
        return {
            "Hello": "World"
        } 

# Routes!
@app.route('/', methods=['GET'])
def index():
    return jsonify(fetch_data())


'''@app.route("/<id>", methods=['GET'])
def get_by_id(id):
    airbnb = db_get_by_id(id)
    if not airbnb:
        return jsonify({"error": "invalid id", "code": 404})
    return jsonify(airbnb)'''


# Runs the API and exposes it on https://<repl name>.<replit username>.repl.co
# ex. Mine deploys to https://htn-api.jayantsh.repl.co.
app.run(host="0.0.0.0", port=5000, debug=True)