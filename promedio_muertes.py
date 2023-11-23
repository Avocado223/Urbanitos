def promedio_muertes(df):
    if df is not None:
        muertes_promedio = df['Muertes'].mean()
        print(f"El promedio diario de muertes es: {muertes_promedio:.2f}")