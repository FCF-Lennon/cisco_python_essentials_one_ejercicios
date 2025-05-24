"""
    Bienvenido a la sección seis, donde aprenderás sobre los tipos de secuencias y el 
    concepto de mutabilidad. Aprenderás sobre las tuplas y los diccionarios, y cómo puedes 
    usarlos para almacenar y procesar valores de datos. ¡Vamos!
"""

"""
    Antes de comenzar a hablar acerca de tuplas y diccionarios, se deben introducir dos conceptos importantes: 
    tipos de secuencia y mutabilidad.

    Un tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar más de un valor 
    (o ninguno si la secuencia esta vacía), los cuales pueden ser secuencialmente (de ahí el nombre) 
    examinados, elemento por elemento.

    Debido a que el bucle for es una herramienta especialmente diseñada para iterar a través de las secuencias, 
    podemos definirlas de la siguiente manera: una secuencia es un tipo de dato que puede ser escaneado por 
    el bucle for.
"""

"""
    La segunda noción - la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe su 
    disponibilidad para poder cambiar libremente durante la ejecución de un programa. Existen dos tipos de datos 
    en Python: mutables e inmutables.

    Los datos mutables pueden ser actualizados libremente en cualquier momento - a esta operación se le denomina "in situ".

    In situ es una expresión en Latín que se traduce literalmente como en posición, en el lugar o momento. Por ejemplo, 
    la siguiente instrucción modifica los datos "in situ": list.append(1)
"""

"""
    Los datos inmutables no pueden ser modificados de esta manera.

    Imagina que una lista solo puede ser asignada y leída. No podrías adjuntar ni remover un elemento de la lista. Si se 
    agrega un elemento al final de la lista provocaría que la lista se cree desde cero.

    Se tendría que crear una lista completamente nueva, la cual contenga los elementos ya existentes más el nuevo elemento.

    El tipo de datos que se desea tratar ahora se llama tupla. Una tupla es una secuencia inmutable. Se puede comportar como 
    una lista pero no puede ser modificada en el momento.
"""

# Tuplas

"""
    Lo primero que distingue una lista de una tupla es la sintaxis empleada para crearlas - las tuplas utilizan paréntesis,
    mientras que las listas usan corchetes, aunque también es posible crear una tupla tan solo separando los valores por comas.
"""
# Se definen dos tuplas ambas contienen 4 elementos
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)
# Nota: cada elemento de una tupla puede ser de distinto tipo (punto flotante, entero, cadena, o cualquier otro tipo de dato).

# Si se desea crear una tupla de un solo elemento, se debe de considerar el hecho de que, debido a la sintaxis 
# (una tupla debe de poder distinguirse de un valor entero ordinario), se debe de colocar una coma al final:

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
one_element_tuple_3 = (1)
one_element_tuple_4 = 1.

print(type(one_element_tuple_1)) # Imprime Tupla
print(type(one_element_tuple_2)) # Imprime Tupla
print(type(one_element_tuple_3)) # Imprime Int
print(type(one_element_tuple_4)) # Imprime Float

# El quitar las comas no arruinará el programa en el sentido sintáctico, pero serán dos variables, no tuplas.

"""
    ¿Qué más pueden hacer las tuplas?

    la función len() acepta tuplas, y regresa el número de elementos contenidos dentro;
    el operador + puede unir tuplas 
    el operador * puede multiplicar las tuplas, así como las listas;
    los operadores in y not in funcionan de la misma manera que en las listas.
"""

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3
t4 = my_tuple
print(len(t2)) # Imprime 9
print(t1) # Imprime (1, 10, 100, 1000, 10000)
print(t2) # Imprime (1, 10, 100, 1, 10, 100, 1, 10 , 100)
print(10 in my_tuple) # Imprime True
print(-10 not in my_tuple) # Imprime True

"""
    Una de las propiedades de las tuplas más útiles es que pueden aparecer en el lado izquierdo del operador 
    de asignación. Este fenómeno ya se vio con anterioridad, cuando fue necesario encontrar una manera de intercambiar 
    los valores entre dos variables.
"""
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1
# Muestra tres tuplas interactuando - en efecto, los valores almacenados en ellas "circulan" entre ellas - t1 se convierte 
# en t2, t2 se convierte en t3, y t3 se convierte en t1.
print(t1, t2, t3)

# -----------------------------------------------------------------------------------------------

# Diccionarios

"""
    El diccionario es otro tipo de estructura de datos de Python. No es una secuencia (pero puede adaptarse fácilmente 
    a un procesamiento secuencial) y además es mutable.

    Para explicar lo que es un diccionario en Python, es importante comprender de manera literal lo que es un diccionario.
"""


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

"""
    Primeramente, recordemos que los diccionarios no son listas - no guardan el orden de sus datos, 
    el orden no tiene significado (a diferencia de los diccionarios reales). El orden en que un diccionario 
    almacena sus datos esta fuera de nuestro control. Esto es normal. (*)

    Nota  
    (*) En Python 3.6x los diccionarios se han convertido en colecciones ordenadas de manera predeterminada. 
    Tu resultado puede variar dependiendo en la versión de Python que se este utilizando. 
"""
 
# Si deseas obtener cualquiera de los valores, debes de proporcionar una clave válida:

""" print(dictionary['cat']) """
print(phone_numbers['Suzy'])

"""
    El obtener el valor de un diccionario es semejante a la indexación, gracias a los corchetes alrededor del valor de la clave.

    Nota:

    si una clave es una cadena, se tiene que especificar como una cadena;
    las claves son sensibles a las mayúsculas y minúsculas: 'Suzy' sería diferente a 'suzy'.

    print(phone_numbers['president'])
 
    Provocará un error de ejecución. Inténtalo.

    Afortunadamente, existe una manera simple de evitar dicha situación. El operador in, junto 
    con su acompañante, not in, pueden salvarnos de esta situación.
"""

# El siguiente código busca de manera segura palabras en francés:
# Cuando escribes una expresión grande o larga, puede ser una buena idea mantenerla alineada verticalmente
dictionary = {
    "cat": "gato", 
    "perro": "chien", 
    "caballo": "cheval"
} # Este tipo de formato se llama sangría francesa.

words = ["gato", "león", "caballo"]

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario.")


# Métodos y funciones de los diccionarios

# Método keys()

"""
    ¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?
    No y si.
    No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.
    Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario 
    a los requerimientos del bucle for (en otras palabras, se construye un enlace intermedio entre 
    el diccionario y una entidad secuencial temporal).

    El primero de ellos es un método denominado keys(), el cual es parte de todo diccionario. 
    El método retorna o regresa una lista de todas las claves dentro del diccionario. Al tener una 
    lista de claves se puede acceder a todo el diccionario de una manera fácil y útil.
"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key]) # Imprime gato -> chat, luego perro -> chein y por ultimo caballo -> cheval

# otra manera de hacerlo es con el método items()
# este metodo retorna una lista de tuplas, donde cada tupla es un par de clave con su valor

for spanish, french in dictionary.items(): # la manera en que la tupla ha sido utilizada como una variable del bucle for.
    print(spanish, "->", french) # Imprime gato -> chat, luego perro -> chein y por ultimo caballo -> cheval


# Modificar, agregar y eliminar valores en el Diccionario

"""
    El asignar un nuevo valor a una clave existente es sencillo - debido a que los diccionarios 
    son completamente mutables, no existen obstáculos para modificarlos.

    Se va a reemplazar el valor "chat" por "minou", lo cual no es muy adecuado, pero funcionará 
    con nuestro ejemplo.
"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['gato'] = 'minou'
print(dictionary) # Imprime {"gato": "minou", "perro": "chien", "caballo": "cheval"}

# funcion sorter()

for key in sorted(dictionary.keys()):
    print(key) # imprime las llaves ordenades alfabeticamente


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# metodo values()
# También existe un método denominado values(), funciona de manera muy similar al de keys(), 
# pero regresa una lista de valores.

for french in dictionary.values():
    print(french) # imprime las claves ordenades alfabeticamente
"""
    Como el diccionario no es capaz de automáticamente encontrar la 
    clave de un valor dado, el rol de este método es algo limitado.
"""

# Agregar nuevas llaves al diccionario

"""
    Agregar una nueva clave con su valor a un diccionario es tan simple como asignar un valor 
    a una clave inexistente. Python añadirá automáticamente esa nueva entrada al diccionario.
"""
# Se asigna una nueva clave ('cisne') con su valor ('cygne')
dictionary['cisne'] = 'cygne' 
print(dictionary) # Imprime: {'gato': 'chat', 'perro': 'chien', 'caballo': 'cheval', 'cisne': 'cygne'}

"""
    Nota: este es un comportamiento muy diferente comparado a las listas, las cuales no permiten 
    asignar valores a índices no existentes.
"""

# Método update()
# También es posible insertar un elemento en el diccionario utilizando el método update()

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
# Se asigna una nueva clave ('pato') con su valor ('canard') 
dictionary.update({"pato": "canard"})
print(dictionary) # Imprime: {'gato': 'chat', 'perro': 'chien', 'caballo': 'cheval', 'pato': 'canard'}

"""
    Nota: El método update() no solo permite agregar nuevas claves, sino también actualizar el valor 
    de claves existentes. Por ejemplo, dictionary.update({"gato": "minou"}) cambiaría el valor de 'gato'.
"""

# Eliminando una clave en el diccionario

"""
    Al eliminar una clave, también se remueve su valor asociado. 
    Los valores no pueden existir sin sus claves.

    Esto se logra usando la instrucción `del`.
"""

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary['perro']  # Elimina un elemento del diccionario según su clave

print(dictionary)  # Imprime: {'gato': 'chat', 'caballo': 'cheval'}

"""
    Nota: Si intentas eliminar una clave que no existe, se generará un error KeyError.
"""

# Alternativa segura: pop()
"""
    Si quieres evitar el error en caso de que la clave no exista, puedes usar el método pop() 
    con un valor por defecto:
"""
dictionary.pop('pez', None)  # No genera error si 'pez' no está presente

# Para Eliminar el último elemento del diccionario con popitem()

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
dictionary.popitem()  # Elimina el último par clave-valor insertado
print(dictionary)  # Ejemplo de salida: {'gato': 'chat', 'perro': 'chien'}

"""
    Nota:
    En Python 3.7 y versiones posteriores, los diccionarios mantienen el orden de inserción, 
    por lo que popitem() elimina el último elemento insertado.
    En versiones anteriores a Python 3.6.7, el orden no está garantizado y popitem() elimina 
    un elemento aleatorio.
"""

# Las tuplas y los diccionarios pueden trabajar juntos

"""
    Problema:
    Crear un programa que calcule el promedio de calificaciones por alumno.

    Requisitos:
    - El usuario ingresa nombres de alumnos seguidos de sus calificaciones (0-10).
    - Los nombres pueden ingresarse en cualquier orden.
    - Una entrada con nombre vacío finaliza el ingreso de datos.
    - Al final, se imprime una lista con los nombres y sus respectivos promedios.

    Nota: Si se ingresa una puntuación vacía o no numérica, generará un ValueError, 
    pero no lo abordaremos aún (se verá en la parte de excepciones).
"""
# Diccionario vacío: claves = nombres de alumnos, valores = tuplas de calificaciones
school_class = {}

while True: # se ingresa a un bucle
    name = input("Ingresa el nombre del estudiante: ")
    if name == "":
        break  # Salir si el nombre está vacío

    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break  # Salir si la calificación está fuera del rango permitido

    # Si el alumno ya existe, se agrega la nueva calificación a su tupla
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)  # Si es nuevo, se crea una tupla con su calificación

# se itera a través de los nombres ordenados de los estudiantes
for name in sorted(school_class.keys()):
    # inicializa los datos necesarios para calcular el promedio (sum y counter)
    adding = 0
    counter = 0
    # se itera a través de la tupla, tomado todas las calificaciones subsecuentes y 
    # actualizando la suma junto con el contador.
    for score in school_class[name]:
        adding += score
        counter += 1
    #  # se calcula e imprime el promedio del alumno junto con su nombre
    print(name, ":", adding / counter) # Imprime el nombre del alumno y su promedio


# Ejercicios

# Pregunta 1: ¿Qué ocurrirá cuando se intente ejecutar el siguiente código?

my_tup = (1, 2, 3)
print(my_tup[2]) # Imprime: 3 

# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?

tup = 1, 2, 3  # Tupla
a, b, c = tup  # Desempaquetado
print(a * b * c)  # Imprime: 6 (1 * 2 * 3)

# Completa el código para emplear correctamente el método count() 
# para contar cuántas veces aparece el número 2 en la tupla.

tup = 1, 2, 3, 2, 4, 5, 6, 2, 8, 2, 8, 9
duplicates = tup.count(2)
print(duplicates) # Imprime: 4

# Pregunta 4: Escribe un programa que una los dos diccionarios (d1 y d2) para crear uno nuevo (d3).

d1 = {"Adam Smith" : "A", "Judy Paxton" : "B+"}
d2 = {"Mary Louis" : "A", "Patrick White" : "C"}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3) # Imprime: {'Adam Smith': 'A', 'Judy Paxton': 'B+', 'Mary Louis': 'A', 'Patrick White': 'C'}

# Pregunta 5: Escribe un programa que convierta la lista my_list en una tupla.

my_list = ["car", "Ford", "flower", "Tulip"]
t = tuple(my_list)

print(t) # Imprime: ("car", "Ford", "flower", "Tulip") 

# Pregunta 6: Escribe un programa que convierta la tupla colors en un diccionario.

colors = (("green", "#000000"), ("blue", "#0000FF"))
colors_dictionary = {}

for k, v in colors:
    colors_dictionary[k] = v

# Otra forma: colors_dictionary = dict(colors)

print(colors_dictionary) # Imprime: {'green': '#000000', 'blue': '#0000FF'}

# Pregunta 7: ¿Que ocurrirá cuando se ejecute el siguiente código?

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
# Se imprime la copia original. El método clear() vacía 
# el diccionario original, pero no afecta a la copia.
print(copy_my_dictionary) # Imprime: {"A": 1, "B": 2}

# Pregunta 8: ¿Cuál es la salida del siguiente programa?

colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb) # Imprime: por cada iteración color : rgb ejemplo: blanco:(255, 255, 255) el rgb como tupla.