import csv

with open('productos.csv', newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        if float(fila["precio"]) > 50:
            print(f"- {fila['nombre']} (ID: {fila['id']}) - {fila['precio']}")
