# 1. Puedes emplear la palabra clave reservada return para decirle a una función 
# que devuelva algún valor. La instrucción return termina la función, por ejemplo:

def multiply(a, b):
    return a * b

print(multiply(3, 4))    # salida: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # salida: None

# El resultado de una función se puede asignar fácilmente a una variable, por ejemplo:

def wishes():
    return "¡Felíz Cumpleaños!"

w = wishes()

print(w)    # salida:¡Felíz Cumpleaños!

# Observa la diferencia en la salida en los siguientes dos ejemplos:

# Ejemplo 1
def wishes():
    print("Mis deseos")
    return "Felíz Cumpleaños"

wishes()    # salida: Mis deseos


# Ejemplo 2
def wishes():
    print("Mis deseos")
    return "Felíz Cumpleaños"

print(wishes())

# salida: 
# Mis deseos
# Felíz Cumpleaños

# Puedes usar una lista como argumento de una función, por ejemplo:

def hi_everybody(my_list):
    for name in my_list:
        print("Hola,", name)

hi_everybody(["Adán", "Juan", "Lucía"])

# Una lista también puede ser un resultado de función, por ejemplo:

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

# ejercicio determine si un año es bisiesto

def is_year_leap(year):

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


"""
Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve 
el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función 
debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos 
no tienen sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.1.6). 
Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de 
la función - este truco acortará significativamente el código.
"""

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


"""
Tu tarea es escribir y probar una función que toma tres argumentos 
(un año, un mes y un día del mes) y devuelve el día correspondiente del año, 
o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos 
de prueba al código. Esta prueba es solo el comienzo.
"""

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None


print(day_of_year(1900, 2, 28))


"""
    Tu tarea es escribir una función que verifique si un número es primo o no.

    La función:

        se llama is_prime;
        toma un argumento (el valor a verificar)
        devuelve True si el argumento es un número primo, y False de lo contrario.

    Sugerencia: intenta dividir el argumento por todos los valores posteriores (comenzando desde 2) 
    y verifica el resto - si es cero, tu número no puede ser un número primo; analiza cuidadosamente 
    cuándo deberías detener el proceso.
"""

def is_prime(valor):
    # si un numero no es primo tendra al menos un divisor menor o igual a su raiz cuadrada
    # valor ** 0.5: para llegar hasta la raíz cuadrada.
    # 1 +: para incluir la raíz cuadrada (por cómo funciona range que excluye el extremo izquierdo).
    # int(...): porque range necesita enteros.
    # que pasa aqui con el numero 2 no entraria en la ejecucion del for 
    # porque en range(2, 2) empieza y termina en el mismo numero, seria un ciclo vacio

    for i in range(2, int(1 + valor ** 0.5)):
        if valor  % i == 0:
            return False
    return True

# el numero 1 no es primo. porque los primos son 
# numeros naturales mayores que 1 que tienen solo dos divisores 
# el 1 y el mismo numero
for i in range(1, 20):
    if is_prime(i + 1): # por eso se le suma 1 al indice para descartarlo
        print(f"{i + 1} es primo") # lo mismo aqui se suma uno para que no se imprima el 1
   

"""
    Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

    Las funciones:

    se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente;
    toman un argumento (el valor correspondiente a sus nombres)
    Complementa el código en el editor y ejecuta tu código y verifica si tu salida es la misma 
    que la nuestra.

    Aquí hay información para ayudarte:

    1 milla = 1609.344 metros.
    1 galón = 3.785411784 litros.
"""

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    km100 = miles * 1609.344 / 1000 / 100
    return liters / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


# _______________________________________________________________


# Pregunta 1: ¿Cuál es la salida del siguiente fragmento de código?

def hi():
    return # La función termina aquí, nada después se ejecuta
    print("¡Hola!")  # Esta línea nunca se ejecuta

hi() # No imprime nada. La función retorna implícitamente None.

# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?

def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))     # Retorna True, porque 5 es un entero
print(is_int(5.0))   # Retorna False, porque 5.0 es un float
print(is_int("5"))   # Retorna None, ya que no hay return para strings

# Pregunta 3: ¿Cuál es la salida del siguiente fragmento de código

def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
# Crea y devuelve una lista con los números pares en el rango de 0 hasta 11 (sin incluir el 11)
print(even_num_lst(11)) # imprime [0, 2, 4, 6, 8, 10]

# Pregunta 4: ¿Cuál es la salida del siguiente fragmento de código?

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
# Crea y devuelve una nueva lista con los elementos de foo elevados al cuadrado
print(list_updater(foo)) # imprime [1, 4, 9, 16, 25]

