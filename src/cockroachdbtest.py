import psycopg2
from psycopg2 import Error

from dotenv import load_dotenv
load_dotenv()

import os
db_url = os.environ.get("db_url")

def fetch_data():
    try:
        #create the connection
        connection = psycopg2.connect(db_url)
        cur = connection.cursor()

        cur.execute("SELECT * FROM Post WHERE location= ")

    except (Exception, Error) as error:
        print("Error: ", error)


#Import this file into the function that submits the data 
fetch_data()


