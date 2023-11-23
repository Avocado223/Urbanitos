import pandas as pd

def guardar_en_excel(df):
     if df is not None:
        df.to_excel("datos_covid.xlsx", index=False)
        print("Datos guardados exitosamente en datos_covid.xlsx")