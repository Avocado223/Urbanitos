def promedio_casos(df):
    if df is not None:
        casos_promedio = df['Casos'].mean()
        print(f"El promedio diario de casos es: {casos_promedio:.2f}")
