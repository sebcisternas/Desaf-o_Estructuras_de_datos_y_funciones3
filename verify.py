import preguntas as p


def verificar(alternativas, eleccion):
    # Devuelve el índice de elección dada
    eleccion_index = ['a', 'b', 'c', 'd'].index(eleccion)

    # Obtener la respuesta correcta de las alternativas
    respuesta_correcta = [alt[1] for alt in alternativas].index(1)  # Encuentra la alternativa marcada como correcta

    # Verificar si la elección del usuario es correcta
    if eleccion_index == respuesta_correcta:
        print('Respuesta Correcta')
        return True
    else:
        print('Respuesta Incorrecta')
        return False



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






