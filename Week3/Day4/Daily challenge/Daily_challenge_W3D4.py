import requests
import psycopg2
import random

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '636231'
DATABASE = 'Countries_W3D4'

# Function to fetch data from REST Countries API
def fetch_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API")
        return None

# Function to insert data into the database
def data_to_db (countries):
    try:
        conn = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        c = conn.cursor()
        for country in countries:
            name = country.get('name', {}).get('common')
            capital = country.get('capital', [''])[0]
            # flag = country.get('flags', [''])[0] if 'flags' in country and country['flags'] else ''
            subregion = country.get('subregion', '')
            population = country.get('population', 0)
            c.execute("INSERT INTO countries (name, capital, subregion, population) VALUES (%s, %s, %s, %s)",
                      (name, capital, subregion, population))
            #  The '%s' symbols in the SQL statement represent placeholders for parameterized queries.
            #  Parameterized queries are used to safely insert data into a database without risking SQL injection attacks.
            conn.commit()
    except psycopg2.Error as e:
        print("Error saving menu item:", e)
        return None
    finally:
        conn.close()

def shuffle_select():
    country_data = fetch_countries()
    if country_data:
        # Shuffle the data and select first 10
        random.shuffle(country_data)
        countries_to_select = country_data[:10]
        data_to_db(countries_to_select)
        print("Data inserted successfully.")
    else:
        print("No data fetched from the API.")

shuffle_select()