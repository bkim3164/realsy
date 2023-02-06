#this file is to be only executed as main and not as anything else

from bs4 import BeautifulSoup
import requests
import psycopg2

from dotenv import load_dotenv
load_dotenv()

import os
db_url = os.environ.get("db_url")

def main():

    connection = psycopg2.connect(db_url)
    cursor = connection.cursor()

    cursor.execute('DROP TABLE agents')
    connection.commit()
    
    
    
    print("Action Completed!")

if __name__ == '__main__':
    main()