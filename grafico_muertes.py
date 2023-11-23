import matplotlib.pyplot as plt

def grafico_muertes(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Fecha'], df['Muertes'], label='Muertes', marker='x', color='red')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad de Muertes')
    plt.title('Evolución de Muertes por COVID-19')
    plt.legend()
    plt.grid(True)
    plt.show()