import matplotlib.pyplot as plt

def grafico_casos(df):
    if df is not None:
        plt.figure(figsize=(10, 6))
        plt.plot(df['Fecha'], df['Casos'], label='Casos', marker='o')
        plt.xlabel('Fecha')
        plt.ylabel('Cantidad de Casos')
        plt.title('Evolución de Casos por COVID-19')
        plt.legend()
        plt.grid(True)
        plt.show()
