from archivo import cargar_txt, guardar_txt
from logica import buscar_por_palabras_clave

def menu():
    """Muestra el menú principal del chatbot."""
    print("\n🧭 Menú del Asistente de Viajes:")
    print("1. Hacer una pregunta")
    print("2. Salir")

def iniciar_chat():
    archivo = "../ASISTENTE_DE_VIAJES.txt"
    preguntas_respuestas = cargar_txt(archivo)

    print("**********************************")
    print("🧳 Bienvenido al Asistente de Viajes.")
    print("**********************************")

    while True:
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
        elif opcion == "2":
            print("👋 ¡Gracias por usar el asistente de viajes! ¡Buen viaje!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    iniciar_chat()
