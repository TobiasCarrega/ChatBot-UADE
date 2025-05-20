from archivo import cargar_txt, guardar_txt
from logica import buscar_por_palabras_clave

### archivo.py
import csv
import json

def cargar_txt(nombre_archivo):
    """Carga preguntas y respuestas desde un archivo .txt."""
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
    """Carga preguntas y respuestas desde un archivo .csv."""
    preguntas_respuestas = []
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector, None)  # omitir encabezado si lo tiene
        for fila in lector:
            if len(fila) >= 2:
                preguntas_respuestas.append((fila[0].strip(), fila[1].strip()))
    return preguntas_respuestas

def cargar_json(nombre_archivo):
    """Carga preguntas y respuestas desde un archivo .json."""
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)
        return [(item['pregunta'], item['respuesta']) for item in data]

def guardar_txt(nombre_archivo, pregunta, respuesta):
    """Guarda una nueva pregunta y respuesta en un archivo .txt."""
    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        archivo.write(f"\n{contar_preguntas(nombre_archivo)+1}) {pregunta.capitalize()}\nRespuesta: {respuesta}\n")

def contar_preguntas(nombre_archivo):
    """Cuenta cuántas preguntas hay en el archivo .txt."""
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return sum(1 for linea in archivo if linea.strip().startswith(tuple("1234567890")))

### logica.py
def buscar_por_palabras_clave(entrada, preguntas_respuestas):
    """Busca la mejor coincidencia entre la entrada del usuario y las preguntas conocidas."""
    entrada = entrada.lower()
    mejor_match = None
    max_coincidencias = 0

    for pregunta, respuesta in preguntas_respuestas:
        palabras_clave = [palabra for palabra in pregunta.lower().split() if len(palabra) > 3]
        coincidencias = sum(1 for palabra in palabras_clave if palabra in entrada)

        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_match = (pregunta, respuesta)

    return mejor_match if max_coincidencias >= 2 else None

def menu():
    #------------------Muestra el menú principal del chatbot.
    print("\n🧭 Menú del Asistente de Viajes:")
    print("1. Hacer una pregunta")
    print("2. Salir")

def iniciar_chat():
    #------------------------Funcion del chatbot.
    archivo = "ASISTENTE_DE_VIAJES.txt"
    preguntas_respuestas = cargar_txt(archivo)

    print("**********************************")
    print("🧳 Bienvenido al Asistente de Viajes.")
    print("**********************************")
    opcion=""
    while opcion!=2:
        #----------------------mientras que se mantenga en el chat va a repetir el chatbot.
        menu()
        opcion = input("Seleccioná una opción: ").strip()

        if opcion == "1":
            entrada = input("✈️ Tu pregunta: ").strip()
            if entrada == "":
                print("⚠️ Por favor, escribí algo.")
                continue

            resultado = buscar_por_palabras_clave(entrada, preguntas_respuestas)
            if resultado:
                print("💬 Respuesta:", resultado[1])
            else:
                print("🤔 No encontré una respuesta. ¿Querés agregarla al archivo? (si/no)")
                opcion = input("> ").strip().lower()
                if opcion == "si":
                    nueva_respuesta = input("✍️ Ingresá la respuesta: ").strip()
                    guardar_txt(archivo, entrada, nueva_respuesta)
                    preguntas_respuestas.append((entrada, nueva_respuesta))
                    print("✅ Pregunta agregada con éxito.")
        else:
            print("❌ Opción inválida.")
    else:
        print("👋 ¡Gracias por usar el asistente de viajes! ¡Buen viaje!")


if __name__ == "__main__":
    iniciar_chat()
