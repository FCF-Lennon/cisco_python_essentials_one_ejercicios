# las funciones reciben argumentos que van entre el nombre de la funcion y los parenticis def name_function(a, b)
# y cuando se invoca una funcion es atrevas de su nombre_function(parametros) se le pasan los paremetros
# estos existen fuera de la funcion y la funcion los recibe como argumentos.

# pueden haber argumentos predefinidos o parametros predefinidos, 
# argumentos posicionales o argumentos con palabras claves
# siempre primero se deben definir los argumento posicionales y luego 
# los con palabras clave de lo contrario dara error de sintaxis al ejecutar introduction(first_name="Pedro", "Ramirez")
# pero siempre predominan los parametros predefinidos al imprimir la salida

def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)

introduction("Jorge", "Pérez") # imprime Jorge Perez
introduction("Enrique") # imprime Enrique Smith
introduction(first_name="Guillermo") # imprime Guillermo Smith


# Ejercicios:

# Pregunta 1: ¿Cuál es la salida del siguiente fragmento de código?

def intro(a="James Bond", b="Bond"):
     print("Mi nombre es", b + ".", a + ".")
 
intro() # Imprime: Mi nombre es Bond. James Bond.


# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?


def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")
 
intro(b="Sean Connery") # Imprime: Mi nombre es Sean Connory. James Bond.


# Pregunta 3: ¿Cuál es la salida del siguiente fragmento de código?


def intro(a, b="Bond"):
    print("Mi nombre es", b + ".", a + ".")
 
intro("Susan") # Imprime: Mi nombre es Bond. Susan.
 

# Pregunta 4: ¿Cuál es la salida del siguiente fragmento de código?
# Al estar un argumento con palabra clave antes de un argumento posicional en la funcion
 
""" 
def add_numbers(a, b=2, c): 
print(a + b + c)
 
add_numbers(a=1, c=3) """ # esto da un error de syntaxis 

