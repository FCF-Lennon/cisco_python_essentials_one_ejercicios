# en python estan las funciones integradas como print() que son propias del lenguaje

# Pregunta 1: La función input() es un ejemplo de:

""" 
    a) una función definida por el usuario
    b) una función integrada / respuesta

"""

# Pregunta 2: ¿Qué es lo que ocurre cuando se invoca una función antes de ser definida? Ejemplo:


"""
    hi() 
    def hi():
        print("hi!")
    No se puede invocar una funcion antes de ser definida en python, esto genera 
    una excepcion de tipo NameError
"""

# Pregunta 3: ¿Qué es lo que ocurrirá cuando se ejecute el siguiente código?


def hi():
    print("hi")
 # esto dara un error de argumento donde se esta enviando uno, 
 # cuando la funcion no recibe argumento o parametro    
hi(5) 