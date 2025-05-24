# Pregunta 1 ¿Cuál de las siguientes líneas inicia correctamente una definición de función sin parámetros?

"""
function fun():
def fun(): / respuesta
def fun:
fun function():
"""

# Pregunta 2 Una función definida de la siguiente manera:  (Elegir dos respuestas)

def function(x=0):
    return x

"""
    opciones:
    debe invocarse sin ningún argumento.
    debe ser invocada con exactamente un argumento.
    puede ser invocada sin ningún argumento. /respuesta
    puede ser invocado con exactamente un argumento./respuesta
"""

# Pregunta 3 Una función integrada es una función que:

"""
    opciones:
    viene con Python, y es una parte integral de Python / respuesta
    tiene que ser importado antes de su uso
    está oculto a los programadores
    ha sido colocado dentro de tu código por otro programador
"""

# Pregunta 4 El hecho de que las tuplas pertenezcan a tipos de secuencia significa que:

"""
    opciones:

    se pueden indexar y rebanar como las listas / respuesta
    en realidad son listas
    se pueden extender usando el método .append()
    se pueden modificar usando la instrucción del
"""

# Pregunta 5 ¿Cuál es la salida del siguiente fragmento de código?

"""
    opciones:

    6 / respuesta
    3
    1
    el codigo es erroneo
"""

# Pregunta 6 ¿Cuál es la salida del siguiente fragmento de código?

def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x) # Imprime: 4

# Pregunta 7 ¿Qué código insertarías en lugar del comentario para obtener el resultado esperado?

"""
    Salida esperada:

    a
    b
    c
"""

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # Inserta tu código aquí.

"""
    opciones:

    print(k[0]) / respuesta
    print(k['0'])
    print(k)
    print(k["0"])
"""


# Pregunta 8 El siguiente fragmento de código:

def func(a, b):
    return a ** a


print(func(2)) # Esto da TypeError porque falta el segundo argumento.

"""
    opciones:

    dará como salida 4
    dará como salida 2
    es erroneo / respuesta 
    devolverá None
"""

# Pregunta 9 El siguiente fragmento de código:

def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))

"""
    opciones:

    es erroneo
    dará como salida 4
    dará como salida 2
    dará como salida 16 / respuesta
"""

# Pregunta 10 ¿Cuál de las siguientes líneas inicia correctamente una función utilizando 
# dos parámetros, ambos con valores predeterminados de cero?

"""
    opciones:

    def fun(a=b=0):
    fun fun(a, b=0):
    fun fun(a=0, b):
    def fun(a=0, b=0): / respuesta
"""

# Pregunta 11 ¿Cuáles de las siguientes afirmaciones son verdaderas? (Selecciona dos respuestas)

"""
    opciones:

    El valor None puede ser comparado con otras variables / respuesta
    El valor None puede ser empleado como argumento de operaciones aritméticas
    El valor None puede ser asignado a variables / respuesta
    El valor None no puede ser empleado fuera de las funciones
"""

# Pregunta 12 ¿Cuál es la salida del siguiente fragmento de código?

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return

print(fun(fun(2)) + 1)

"""
    opciones:

    2
    el código provocará un error de tiempo de ejecución / respuesta
    1
    None
"""

# Pregunta 13 ¿Cuál es la salida del siguiente fragmento de código?

def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)

"""
    opciones:

    Ninguno
    el código provocará un error de tiempo de ejecución
    4 / respuesta
    2
"""

# Question 14 ¿Cuál es la salida del siguiente fragmento de código?

def any():
    print(var + 1, end='')

var = 1
any()
print(var)

"""
    22
    21 / respuesta
    12
    11
"""

# Pregunta 15 Asumiendo que my_tuple es una tupla creada correctamente, 
# el hecho de que las tuplas son inmutables significa que la siguiente instrucción:

"""
    my_tuple[1] = my_tuple[1] + my_tuple[0]

    opciones:

    puede ser ilegal si la tupla contiene cadenas
    es completamente correcta
    puede ser ejecutada solo si la tupla contiene al menos dos elementos
    es ilegal / respuesta  
"""

# Pregunta 16 ¿Cuál es la salida del siguiente fragmento de código?

my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'

print(my_list(my_list)) 

"""
    opciones: 

    ['Mary', 'had', 'a', 'lamb']
    ['Mary', 'had', 'a', 'ram']
    ['Mary', 'had', 'a', 'little', 'lamb']
    no hay salida / respuesta
"""

# Pregunta 17 ¿Cuál es la salida del siguiente fragmento de código?

def fun(x, y, z):
    return x + 2 * y + 3 * z
print(fun(0, z=1, y=3))

"""
    9 / respuesta
    3
    0
    el código es erroneo
"""

# Pregunta 18 ¿Cuál es la salida del siguiente fragmento de código?

def fun(inp=2, out=3):
    return inp * out
print(fun(out=2)) # Imprime: 4

# Pregunta 19 ¿Cuál es la salida del siguiente código?

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
 
for k in range(len(dictionary)):
    v = dictionary[v]
 
print(v)

"""
    opciones:

    three
    two / respuesta
    one
    ('one', 'two', 'three')
"""

# Pregunta 20 ¿Cuál es la salida del siguiente código?

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

"""
    opciones:

    (2)
    (2, )
    2 / respuesta
    el código es erroneo
"""

# Pregunta 21 Selecciona las sentencia true sobre el bloque try-except en relación con el siguiente ejemplo. 
# (Selecciona dos respuestas).

"""
    try:
    # Algo de código...
except:
    # Algo de código...
"""

"""
    opciones:

    Si existe un error de sintaxis en el código ubicado en el bloque try, la sentencia except no lo manejará, 
    y una excepción SyntaxError será generada.
    El código que sigue a la sentencia except será ejecutado si el código en el bloque try se encuentra con un error. / respueta
    El código que sigue a la sentencia try será ejecutado si el código dentro de la sentencia except se encuentra con un error.
    Si sospechas que un fragmento de código puede generar una excepción, se debe colocar dentro del bloque try. / respuesta
"""

# Pregunta 22 ¿Cuál es la salida del siguiente código?

try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")

"""
    opciones:

    Entrada muy errónea... / respuesta
    Entrada errónea...
    ¡Buuu!
    Entrada incorrecta...
"""