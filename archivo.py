import csv
import json
import os


def cargar_txt(nombre_archivo):
    # Carga preguntas y respuestas desde un archivo .txt.
    preguntas_respuestas = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        pregunta_actual = ""
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("Respuesta:"):
                respuesta = linea.replace("Respuesta:", "").strip()
                preguntas_respuestas.append((pregunta_actual, respuesta))
            elif linea != "" and ")" in linea and linea[0].isdigit():
                pregunta_actual = linea.split(")", 1)[1].strip()
    return preguntas_respuestas

def cargar_csv(nombre_archivo):
    # Carga preguntas y respuestas desde un archivo .csv
    preguntas_respuestas = []
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector, None)  # omitir encabezado si lo tiene
        for fila in lector:
            if len(fila) >= 2:
                preguntas_respuestas.append((fila[0].strip(), fila[1].strip()))
    return preguntas_respuestas

def cargar_json(nombre_archivo):
    # Carga preguntas y respuestas desde un archivo .json
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)
        return [(item['pregunta'], item['respuesta']) for item in data]

def guardar_txt(nombre_archivo, pregunta, respuesta):
    # Guarda una nueva pregunta y respuesta en un archivo .txt
    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        archivo.write(f"\n{contar_preguntas(nombre_archivo)+1}) {pregunta.capitalize()}\nRespuesta: {respuesta}\n")

def guardar_csv(nombre_archivo, pregunta, respuesta):
    # Guarda una nueva pregunta y respuesta en un archivo .csv
    crear_encabezado = not os.path.exists(nombre_archivo)
    with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        if crear_encabezado:
            writer.writerow(["pregunta", "respuesta"])
        writer.writerow([pregunta, respuesta])

def guardar_json(nombre_archivo, pregunta, respuesta):
    # Guarda una nueva pregunta y respuesta en un archivo .json
    data = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            try:
                data = json.load(archivo)
            except json.JSONDecodeError:
                data = []
    data.append({"pregunta": pregunta, "respuesta": respuesta})
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(data, archivo, ensure_ascii=False, indent=2)

def contar_preguntas(nombre_archivo):
    # Cuenta cuántas preguntas hay en el archivo .txt
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return sum(1 for linea in archivo if linea.strip().startswith(tuple("1234567890")))
