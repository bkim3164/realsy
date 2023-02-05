import psycopg2
from psycopg2 import Error

db_url = 'postgresql://brian:rtsNRr0uzXSWexZupx9wxw@forest-grizzly-4869.6wr.cockroachlabs.cloud:26257/forest-grizzly-4869.defaultdb?sslmode=verify-full'


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


