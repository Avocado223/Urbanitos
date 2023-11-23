import requests
import pandas as pd

def obtener_datos():
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        dates = list(data["cases"].keys())
        df = pd.DataFrame({
            "Fecha": dates,
            "Casos": list(data["cases"].values()),
            "Muertes": list(data["deaths"].values())
        })
        return df
    else:
        print("La solicitud no fue exitosa; Estado:", response.status_code)
        return None