# 1. Una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función. 
# (Ejemplo 1) al menos que la función defina una variable con el mismo nombre. 
# (Ejemplo 2, y Ejemplo 3), por ejemplo:

# Ejemplo 1:

var = 2
 
def mult_by_var(x):
    return x * var
 
print(mult_by_var(7)) # salida: 14
 
# Ejemplo 2:

def mult(x):
    var = 5
    return x * var
 
print(mult(7)) # salida: 35

# Ejemplo 3:

def mult(x):
    var = 7
    return x * var
 
var = 3
print(mult(7)) # salida: 49
 
# 2. Una variable que existe dentro de una función tiene un alcance solo dentro 
# del cuerpo de la función (Ejemplo 4), por ejemplo:

# Ejemplo 4:

def adding(x):
    var = 7
    return x + var
 
print(adding(4)) # salida: 11
print(var) # NameError
 
# 3. Se puede emplear la palabra clave reservada global seguida por el nombre de 
# una variable para que el alcance de la variable sea global, por ejemplo:

var = 2
print(var) # salida: 2
 
def return_var():
    global var
    var = 5
    return var
 
print(return_var()) # salida: 5
print(var) # salida: 5


# Ejercicios:

# Pregunta 1: ¿Cuál es la salida del siguiente fragmento de código?

def message():
    alt = 1
    print("¡Hola, mundo!")

# print(alt)  # Error: 'alt' no está definido en el ámbito global

# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?

a = 1
 
def fun():
    a = 2 # Esta 'a' es una variable local dentro de la función
    print(a)
 
fun()      # Imprime: 2 (usa la variable local)
print(a)   # Imprime: 1 (la variable global 'a' no fue modificada)

# Pregunta 3: ¿Cuál es la salida del siguiente fragmento de código?

a = 1
 
def fun():
    global a  # Indica que se usará la variable global 'a'
    a = 2     # Modifica la variable global
    print(a)
 
fun()      # Imprime: 2 (se modifica e imprime la variable global)
a = 3      # Se vuelve a modificar la variable global fuera de la función
print(a)   # Imprime: 3

# Pregunta 4: ¿Cuál es la salida del siguiente fragmento de código?

a = 1

def fun():
    global a  # Se refiere a la variable global 'a'
    a = 2     # Modifica la variable global
    print(a)

a = 3        # Se modifica la variable global antes de llamar a la función
fun()        # Imprime: 2 (la función cambia el valor global a 2)
print(a)     # Imprime: 2 (se muestra el nuevo valor de la variable global)

