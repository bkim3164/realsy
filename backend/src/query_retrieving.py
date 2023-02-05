import psycopg2
import agent_data_scrapper
import query_sending

db_url = 'postgresql://Realsy:JmUsz3HAW98i65TP389vPA@forest-grizzly-4869.6wr.cockroachlabs.cloud:26257/forest-grizzly-4869.defaultdb?sslmode=verify-full'

def main(location, x = False):
    print(f'Given Location type:{ type(location)}')
    print(f"given Location: {location}")
    #this will be the input in the future

    #create the connection
    connection = psycopg2.connect(db_url)
    cursor = connection.cursor()

    #execute retrieval from database
    cursor.execute("SELECT name,firm,number,experience,sold FROM agents WHERE location = %s;",(location,))
    results = cursor.fetchall()


    if len(results) == 0 and x == False:
        print('Info not found in database, trying to retrieve from website...')
        city, state = location.split(',')
        city = city.replace(' ', '_')
        scrapped_info: dict = agent_data_scrapper.main(city, state)
        query_sending.main(scrapped_info)
        return main(location, True)

    print("Successfully retrieved information from the database!")


    # THIS is for debugging

    #for result in results:
    #    print(result)

    return results


if __name__ == '__main__':
    i_location = 'irvine,CA'
    main(i_location)

