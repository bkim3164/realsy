#this file is to be only executed as main and not as anything else

from bs4 import BeautifulSoup
import requests
import psycopg2

db_url = 'postgresql://Realsy:JmUsz3HAW98i65TP389vPA@forest-grizzly-4869.6wr.cockroachlabs.cloud:26257/forest-grizzly-4869.defaultdb?sslmode=verify-full'

def main():

    connection = psycopg2.connect(db_url)
    cursor = connection.cursor()

    cursor.execute('DELETE FROM agents;')
    connection.commit()



if __name__ == '__main__':
    pass