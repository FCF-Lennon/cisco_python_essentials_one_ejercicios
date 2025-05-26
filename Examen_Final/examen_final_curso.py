# Pregunta 1 ¿Cuál es el resultado del siguiente fragmento de código?

my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list) # Imprime: [1, 1, 1, 2]

# Pregunta 2 El significado de un argumento posicional está determinado por:

"""
    opciones:

    su conexión con variables existentes
    su valor
    su posición dentro de la lista de argumentos / respuesta
    el nombre del argumento especificado junto con su valor
"""

# Pregunta 3 ¿Cuáles de los siguientes enunciados son verdaderos respecto al código? (Selecciona dos respuestas)

nums = [1, 2, 3]
vals = nums

"""
    opciones:

    nums y vals son listas diferentes
    vals es más larga que nums
    nums tiene la misma longitud que vals / respuesta
    nums y vals son diferentes nombres de la misma lista / respuesta
"""

# Pregunta 4 Un operador capaz de verificar si dos valores no son iguales se codifica como:

"""
    not ==
    <>
    =/=
    != / respuesta
"""

# Pregunta 5 El siguiente fragmento de código:

def function_1(a):
    return None

def function_2(a):
    return function_1(a) * function_1(a)

# print(function_2(2))

"""
    opciones:

    dará como salida 16
    provocará un error de ejecución / respuesta
    dará como salida 2
    dará como salida 4
"""

# Pregunta 6 El resultado de la siguiente división:

1 // 2

"""
    opciones:

    es igual a 0.0
    es igual a 0.5
    es igual a 0 / respuesta
    no se puede predecir
"""

# Pregunta 7 El siguiente fragmento de código:

def func(a, b):
    return b ** a

# print(func(b=2, 2))

"""
    opciones:

    dará como salida None
    es erróneo / respuesta
    dará como salida 4
    dará como salida 2
"""

# Pregunta 8 ¿Qué valor se asignará a la variable x?

z = 0 
y = 10
x = y < z and z > y or y < z and z < y

"""
    opciones:

    0
    1
    True
    False / respuesta
"""

# Pregunta 9 ¿Cualés de los siguientes nombres de variable son Ilegales y provocarán 
# una excepción de SyntaxError? (Selecciona dos respuestas)

"""
    opciones:

    In
    for / respuesta
    print
    in / respuesta
"""

# Pregunta 10 ¿Cuál es el resultado dle siguiente fragmento de código?

my_list = [x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))

"""
    opciones:

    [1, 4, 9, 16]
    [0, 1, 4, 16]
    [0, 1, 9, 16] 
    [0, 1, 4, 9] / respuesta
"""

# Pregunta 11 ¿Cuál es el resultado del siguiente fragmento de código?

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

"""
    2 1 2
    1 2 1
    1 2 2
    1 1 2 / respuesta
"""

# Pregunta 12 ¿Cuál es el resultado del siguiente fragmento de código?

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

"""
    opciones: 

    0 0
    1 1
    1 0
    0 1 / respuesta
"""

# Pregunta 13 ¿Cuál es el resultado del siguiente fragmento de código?

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
    
print(fun(fun(2)))

"""
    opciones:

    None
    1
    el código provocará un error de ejecución
    2 / respuesta
"""

# Pregunta 14 Observa el fragmento de código y elige la sentencia verdadera:

nums = [1, 2, 3]
vals = nums
del vals[:]

"""
    opciones:

    el código provocará un error de ejecución
    vals es más larga que nums
    nums y vals tienen la misma longitud / respuesta
    nums es más larga que vals
"""

# Pregunta 15 ¿Cúal es el resultado del siguiente fragmento 
# de código si el usuario ingrasa dos líneas que contienen 3 y 2 respectivamente?

x = int(input())
y = int(input())
x = x % y 
x = x % y
y = y % x
print(y)

"""
    opciones:

    2
    0 / respuesta
    1
    3
"""

# Pregunta 16 ¿Cuál es el resultado del siguiente fragmento de código si el 
# usuario ingresa dos líneas que contienen 3 y 6 respectivamente?

y = input()
x = input()
print(x + y)

"""
    6
    3
    63 / respuesta
    36 
"""

# Pregunta 17 ¿Cuál es el resultado del siguiente fragmento de código?

print("a", "b", "c", sep=("sep"))

"""
    opciones:

    abc
    a b c
    asepbsepcsep
    asepbsepc / respuesta
"""

# Pregunta 18 ¿Cuál es el resultado del siguiente fragmento de código?

x = 1 // 5 + 1 / 5
print(x)

"""
    opciones:

    0.5
    0.4
    0
    0.2 / respuesta
"""

# Pregunta 19 Suponiendo que my_tuple es una tupla creada correctamente,
# el hecho que las tuplas sean inmutables significa que la siguiente instrucción:

# my_tuple[1] = my_tuple[1] + my_tuple[0]

"""
    opciones:

    es completamente correcta
    se puede ejecutar si y solo si la tupla contiene al menos dos elementos
    puede ser ilegal si la tupla contiene cadenas
    es ilegal / respuesta
"""

# Pregunta 20

# ¿Cuál es el resultado del siguiente fragmento de codigo
# si el usuario ingresa dos líneas que contienen 2 y 4 respectivamente?

x = float(input())
y = float(input())
print(y ** (1/x))

"""
    opciones:

    2.0 / respuesta
    1.0
    4.2
    0.0
"""

# Pregunta 21 ¿Cuál es el resultado del siguiente fragmento de código?

dct = {
    "one":"two",
    "three":"one", 
    "two":"three"
}
v = dct["three"]

for k in range(len(dct)):
    v = dct[v]
print(v)

"""
    opciones:

    three
    one / respuesta
    two
    {"one", "two", "three"}
"""

# Pregunta 22 ¿Cuántos alementos contiene la lista lst?

lst = [i for i in range(-1, -2)]

"""
    opciones:

    dos
    cero / respuesta
    uno
    tres
"""

# Pregunta 23 ¿Cuáles de las siguientes lineas correctamente 
# invocan la función definida a continuación? (Selecciona dos respuetas)

# def fun(a, b, c=0):

"""
    opciones:

    fun(b=0, a=0) / respuesta
    fun()
    fun(b=1)
    fun(0, 1, 2) / respuesta
"""

# Pregunta 24 ¿Cuál es el resultado del siguiente fragmento de código?

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y - 1)

print(fun(0, 3))

"""
    0 / respuesta
    2
    el código provocará un error de ejecución
    1
"""

# Pregunta 25 ¿Cuántos (*) imprimirá el siguiente fragmento de código en la consola?

i = 0
while i < i + 2:
    i += 1
    print("*")
else:
    print("*")

"""
    opciones:

    1
    2
    el fragmento entrará en un bulcle infinito, imprimiendo un * por linea / respuesta
    0
"""

# Pregunta 26 ¿Cuál es el resultado del siguiente fragmento de código?

tup = (1, 2, 3, 4, 5)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

"""
    opciones:

    44
    (4)
    4 / respuesta
    (4,)
"""

# Pregunta 27 ¿Cuál es el resultado del siguiente fragmento de código?

dd = {"1":"0", "0":"1"}

for x in dd.vals():
    print(x, end="")

"""
    opciones:

    el código es erróneo (el objeto dict no contiene el método vals()) / respuesta
    1 0
    0 0
    0 1
"""

# Pregunta 28 ¿Cuál es el resultado del siguiente fragmento de código?

dct = {}
dct["1"] = (1, 2)
dct["2"] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

"""
    opciones:

    (2, 1)
    (1, 2)
    12
    21 / respuesta
"""

# Pregunta 29 ¿Cuál es el resultado del siguiente fragmento de código?

def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))

"""
    opciones:

    6
    2
    4 / respuesta
    el fragmento de código es erróneo y provocará un SyntaxError
"""

# Pregunta 30 ¿Cuántos (*) imprimirá el siguiente fragmento de código en la consola?

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

"""
    opciones:

    cero
    nueve
    tres / respuesta
    seis 
"""

# Pregunta 31 ¿Cuál es el comportamiento esperado del siguiente programa si el usuario ingresa 0?

try: 
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...") 
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")


"""
    opciones:

    Entrada errónea... 
    ¡Buuu!
    Entrada incorrecta...
    1.0
    0.0 / respuesta
    Entrada muy errónea...
"""

# Pregunta 32 ¿Cúal es el comportamiento esperado del siguiente programa?

""" 
try:
    print(5/0)
    break
except:
    print("Lo siento, algo salió mal...")
except (ValueError, ZeroDivisionError):
    print("Mala suerte...") 
"""

"""
    opciones:

    El programa provocará una excepción SyntaxError. / Respuesta

    El programa provocará una excepción ZeroDivisionError y dará como salida 
    el siguiente mensaje: Mala suerte...

    El programa provocará una excepción ValueError y dará como salida un mensaje 
    de error predeterminado.

    El programa generará una excepción y será manejada por el primer bloque except.

    El programa provocará una excepción ValueError y dará como salida el siguiente 
    mensaje: Mala suerte...

    El programa provocará una excepción ZeroDivisionError y dará como salida un 
    mensaje de error predeterminado.
"""

# Pregunta 33 ¿Cuál es el comportamiento esperado del siguiente programa?

foo = (1, 2, 3)
foo.index(0)

"""
    opciones:

    El programa provocará una excepción ValueError. / Respuesta
    El programa provocará una excepción TypeError.
    El programa dará como salida un 1 en la pantalla.
    El programa provocará una excepción AttributeError.
    El programa provocará una excepción SyntaxError.
"""

# Pregunta 34 ¿Cuál de los siguientes fragmentos muestra la forma correcta 
# de manejar múltiples excepciones en una sola cláusula except?

"""
    # A:
except (TypeError, ValueError, ZeroDivisionError):
    # Algo de código.
 
# B:
except TypeError, ValueError, ZeroDivisionError:
    # Algo de código.
 
# C:
except: (TypeError, ValueError, ZeroDivisionError)
    # Algo de código.
 
# D:
except: TypeError, ValueError, ZeroDivisionError
    # Algo de código.
 
# E:
except (TypeError, ValueError, ZeroDivisionError)
    # Algo de código.
 
# F:
except TypeError, ValueError, ZeroDivisionError
    # Algo de código.
"""

"""
    opciones:

    A solamente / Respuesta
    B y C
    A y F
    F solamente
    A y B 
    A, C y D
    D y E
"""

# Pregunta 35 ¿Qué pasará cuando intentes ejecutar el siguiente código?

# print(¡Hola, Mundo!)

"""
    El código imprimirá ¡Hola, Mundo! en la consola.
    El código generará la excepción SyntaxError. / Respuesta
    El código generará la excepción TypeError.
    El código generará la excepción ValueError.
    El código generará la excepción AttributeError.
"""