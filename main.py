import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Curitiba"
DB_URL = os.getenv("DATABASE_URL")

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get(url)
    data = response.json()

    weather = {
        "cidade": city,
        "temperatura": data["main"]["temp"],
        "umidade": data["main"]["humidity"],
        "descricao": data["weather"][0]["description"],
        "data_coleta": datetime.utcnow()
    }

    return pd.DataFrame([weather])

def save_to_postgres(df):
    engine = create_engine(DB_URL)
    df.to_sql("clima", engine, if_exists="append", index=False)
    print("Dados salvos com sucesso!")

if __name__ == "__main__":
    df = get_weather_data(CITY)
    save_to_postgres(df)
