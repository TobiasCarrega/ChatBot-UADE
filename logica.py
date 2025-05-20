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
