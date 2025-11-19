import csv

from collections import defaultdict
fichero = "la-liga-2025-UTC.csv"
def cargar_resultados(ruta_csv: str) -> list:
    """Lee el archivo CSV y devuelve una lista de partidos."""
    partidos = []
    print("Carga el fichero: ", ruta_csv)
    with open(ruta_csv, encoding = 'utf-8') as f:
        lector = csv.DictReader(f)
#       print("lector: ", lector)
#       print("Longitud lector: ", dir(lector))
#       print("Longitud lector: ", lector.__sizeof__())
        i=0
        for fila in lector:
            i=i+1
#           print("  i:", i)
#           print("Fila : ", fila)
            partidos.append(fila)
#       print("Partidos: ", partidos)
    return partidos

partidos = cargar_resultados("la-liga-2025-UTC.csv")
print(partidos)