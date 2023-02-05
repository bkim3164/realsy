from flask import Flask, jsonify, request
import json
import os
import psycopg2
from flask_cors import CORS, cross_origin
import query_retrieving


# Create a Flask server.
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Create a cursor and initialize psycopg
db_url = 'postgresql://brian:rtsNRr0uzXSWexZupx9wxw@forest-grizzly-4869.6wr.cockroachlabs.cloud:26257/forest-grizzly-4869.defaultdb?sslmode=verify-full'

connection = psycopg2.connect(db_url)
cursor = connection.cursor()



@app.route('/get-location', methods=['POST']) 
def get_(): # handle the POST request 
    if request.method == 'POST': 
        print(request.get_json())
        location = request.get_json()['location']
        print(location)
        data = query_retrieving.main(str(location))
        return {
            "data":data
        } 





# Runs the API and exposes it on https://<repl name>.<replit username>.repl.co
# ex. Mine deploys to https://htn-api.jayantsh.repl.co.
app.run(host="0.0.0.0", port=8000, debug=True)