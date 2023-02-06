import psycopg2
import agent_data_scrapper
import query_sending

from dotenv import load_dotenv
load_dotenv()

import os
db_url = os.environ.get("db_url")

def main(location, x = False):
    #this will be the input in the future

    #create the connection
    connection = psycopg2.connect(db_url)
    cursor = connection.cursor()

    #execute retrieval from database
    cursor.execute("SELECT name,firm,number,experience,sold,image FROM agents WHERE location = %s;",(location,))
    results = cursor.fetchall()


    if len(results) == 0 and x == False:
        print('Info not found in database, trying to retrieve from website...')
        city, state = location.split(',')
        city = city.replace(' ', '-')
        scrapped_info: dict = agent_data_scrapper.main(city, state)
        query_sending.main(scrapped_info)
        return main(location, True)


    if len(results) == 0 and x == True:
        print("Invalid Input, no info found!")
        return None
        

    print("Successfully retrieved information from the database!")


    # THIS is for debugging
    for result in results:
       print(result)

    return results


if __name__ == '__main__':
    i_location = 'irvine,ca'
    main(i_location)

