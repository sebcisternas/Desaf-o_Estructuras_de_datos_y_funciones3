import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    print(enunciado)
    
    # lista de letras asociadas a las alternativas
    letras = ['A', 'B', 'C', 'D']
    
    # imprimir cada alternativa con su letra asociada
    for letra, alternativa in zip(letras, alternativas):
        print(f"{letra}. {alternativa[0]}") 
    
    
   
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4