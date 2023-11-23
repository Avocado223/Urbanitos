def cantidad_anual(df):
    if df is not None:
        casos_anuales = df['Casos'].sum()
        muertes_anuales = df['Muertes'].sum()
        print(f"La cantidad total de casos anuales es: {casos_anuales}")
        print(f"La cantidad total de muertes anuales es: {muertes_anuales}")