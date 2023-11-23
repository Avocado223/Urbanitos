from obtener_datos import obtener_datos
from guardar_en_excel import guardar_en_excel
from grafico_casos import grafico_casos
from grafico_muertes import grafico_muertes
from promedio_casos import promedio_casos
from promedio_muertes import promedio_muertes
from cantidad_anual import cantidad_anual
def menu():
    df = obtener_datos()
    if df is None:
        return

    while True:
        print("\nMenu:")
        print("1) Guardar archivo en Excel")
        print("2) Generar gráfico de casos")
        print("3) Generar gráfico de muertes")
        print("4) Promedio de casos por día")
        print("5) Promedio de muertes diarias")
        print("6) Cantidad de casos anuales y muertes anuales")
        print("7) Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            guardar_en_excel(df)
        elif opcion == '2':
            grafico_casos(df)
        elif opcion == '3':
            grafico_muertes(df)
        elif opcion == '4':
            promedio_casos(df)
        elif opcion == '5':
            promedio_muertes(df)
        elif opcion == '6':
            cantidad_anual(df)
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 7.")