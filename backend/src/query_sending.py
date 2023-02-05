import psycopg2
import agent_data_scrapper

db_url = 'postgresql://Realsy:JmUsz3HAW98i65TP389vPA@forest-grizzly-4869.6wr.cockroachlabs.cloud:26257/forest-grizzly-4869.defaultdb?sslmode=verify-full'

#agents_data = agent_data_scrapper.main('irvine','CA')

def main(agents_data: dict):
    #create the connection
    connection = psycopg2.connect(db_url)
    cursor = connection.cursor()

    #table create initalize
    table_query = "CREATE TABLE IF NOT EXISTS Agents (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), name STRING, firm STRING, number STRING, experience STRING, sold INT4, location STRING);"


    #input values in table
    order = "name,firm,number,sold,experience,location"
    for agent_info in agents_data.items():
        #print(agent_info[1])
        cursor.execute(f"INSERT INTO Agents ({order}) VALUES (%s,%s,%s,%s,%s,%s);",agent_info[1])

    
    connection.commit()
    print("Updated information to database.")


if __name__ == "__main__":
    pass
        