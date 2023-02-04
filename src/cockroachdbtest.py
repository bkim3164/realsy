import psycopg2
from psycopg2 import Error

db_url = 'postgresql://Realsy:JmUsz3HAW98i65TP389vPA@forest-grizzly-4869.6wr.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full'


def create_table():
    try:
        #create the connection
        connection = psycopg2.connect(db_url)
        cursor = connection.cursor()

        #SQL query
        create_table_query = "CREATE TABLE IF NOT EXISTS test (id INT PRIMARY KEY, title STRING, price INT);"
        cursor.execute(create_table_query)

        #commit query and print results
        connection.commit()
        print("Table created!")

    except (Exception, Error) as error:
        print("Error: ", error)


create_table


