import requests
import pandas as pd

API_KEY = "5f59439547a44c3891f18650d700bd19"
CITIES = ["London", "Katowice", "Warsaw"]

def fetch_weather_data():
    data = []
    
    for city in CITIES:
        url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={API_KEY}&units=M"
        response = requests.get(url).json()
        
        if "data" in response:  # Check if the API response is valid
            weather = response["data"][0]  # Extract first item from "data" list
            data.append({
                "city": city,
                "temperature": weather["temp"],
                "humidity": weather["rh"],  # "rh" is relative humidity in Weatherbit API
                "timestamp": pd.Timestamp.now()
            })
        else:
            print(f"Error fetching data for {city}: {response}")
    
    return pd.DataFrame(data)

# Example usage
df = fetch_weather_data()
print(df)

def transform_data(df):
    # Ensure numeric columns
    df["temperature"] = pd.to_numeric(df["temperature"])
    df["humidity"] = pd.to_numeric(df["humidity"])
    return df

from sqlalchemy import create_engine

# Replace with your MySQL connection details
username = 'root'
password = 'Joemarocha1@'
host = '127.0.0.1'  # e.g., 'localhost'
database = 'weather_db'

# Create a connection string for MySQL
connection_string = "mysql+pymysql://root:Joemarocha1%40@127.0.0.1:3306/weather_db"



# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Load the DataFrame into the MySQL table
df.to_sql("weather", engine, if_exists="append", index=False)

# Pull historical data from MySQL and export to CSV
def export_data_to_csv():
    # Query the database to get all historical data
    query = "SELECT * FROM weather;"
    historical_df = pd.read_sql(query, engine)

     # Export historical data to CSV
    historical_df.to_csv("weather_data.csv", index=False)
    print("Historical weather data exported to weather_data.csv")

def load_data_to_mysql(df):
    # Replace with your MySQL connection details
    username = 'root'
    password = 'Joemarocha1@'
    host = '127.0.0.1'  # e.g., 'localhost'
    database = 'weather_db'
    
    # Create a connection string for MySQL
    connection_string = "mysql+pymysql://root:Joemarocha1%40@127.0.0.1:3306/weather_db"
    
    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)

    # Load the DataFrame into the MySQL table
    df.to_sql("weather", engine, if_exists="append", index=False)
    print("Data loaded to MySQL database")


# Main script
if __name__ == "__main__":
    # Fetch, transform, and load data
    df = fetch_weather_data()
    df = transform_data(df)
    load_data_to_mysql(df)
    
    # Export historical data from MySQL to CSV
    export_data_to_csv()