from obtener_datos import obtener_datos
from guardar_en_excel import guardar_en_excel
from grafico_casos import grafico_casos
from grafico_muertes import grafico_muertes
from promedio_casos import promedio_casos
from promedio_muertes import promedio_muertes
from cantidad_anual import cantidad_anual
from menu import menu 

df = obtener_datos()
if df is not None:
    menu()