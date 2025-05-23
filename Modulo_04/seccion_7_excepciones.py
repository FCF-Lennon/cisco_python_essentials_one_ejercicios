"""
    Excepciones en Python
    En Python, existen dos grandes tipos de errores:

    1. Errores de Sintaxis
    Son errores detectados por el analizador de código antes de ejecutar el programa. Suceden 
    cuando escribes algo incorrecto en cuanto a las reglas del lenguaje.

    Ejemplo:
    print("Hola, ¡Mundo!)

    Este código provocará un error de tipo SyntaxError, debido a que falta una comilla al final 
    de la cadena.

    Salida del error:

    File "main.py", line 1
        print("Hola, ¡Mundo!)
                            ^
    SyntaxError: EOL while scanning string literal
"""

# Observa cómo la flecha apunta al problema exacto: falta una comilla doble (").

"""
    2. Excepciones
    Las excepciones ocurren durante la ejecución, incluso si el código es sintácticamente 
    correcto. Estas reflejan errores como divisiones por cero o tipos de datos inválidos.

    Ejemplo:
    print(1 / 0)

    Salida del error:

    Traceback (most recent call last):
    File "main.py", line 1, in <module>
        print(1 / 0)
    ZeroDivisionError: division by zero
"""
# El mensaje describe el tipo de excepción (ZeroDivisionError) y el contexto del error.

"""
    Manejo de Excepciones con try-except

    Python te permite manejar excepciones con try y except, evitando que tu programa se 
    detenga inesperadamente.
"""

while True:
    try:
        number = int(input("Ingresa un número entero: "))
        print(number/2)
        break
    except:
        print("Advertencia: el valor ingresado no es un número válido. Intenta de nuevo...")

"""
    ¿Qué sucede aquí?

    1. El usuario ingresa un valor.
    2. Si el valor no es convertible a entero, se lanza una excepción.
    3. El bloque except captura el error y muestra un mensaje de advertencia.
    4. El bucle repite hasta que se ingrese un número válido.
"""

# Múltiples bloques except
# Puedes capturar diferentes tipos de excepciones con bloques separados:

while True:
    try:
        number = int(input("Ingresa un número entero: "))
        print(5/number)
        break
    except ValueError:
        print("Valor incorrecto.")
    except ZeroDivisionError:
        print("Lo siento. No puedo dividir entre cero.")
    except:
        print("No se que hacer...")

"""
    a) ValueError captura entradas no numéricas.
    b) ZeroDivisionError detecta divisiones por cero.
    c) El bloque except genérico captura cualquier otra excepción. Este debe ir al final.
"""

# Captura múltiple en un solo except 
# También puedes capturar varios errores en una misma línea:

while True:
    try:
        number = int(input("Ingresa un número entero: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor incorrecto o se ha roto la regla de división entre cero.")
    except:
        print("Lo siento, algo salió mal...")

"""
    Algunas excepciones comunes en Python:

    a) ZeroDivisionError: división por cero
    b) ValueError: valor no válido (como convertir "abc" a int)
    c) TypeError: operación entre tipos incompatibles
    d) AttributeError: acceso a un atributo que no existe
    e) SyntaxError: error de escritura en el código
    f) KeyboardInterrupt: cuando el usuario presiona Ctrl+C para interrumpir el programa
    g) Prueba presionar Ctrl+C cuando corras el código para ver cómo se lanza KeyboardInterrupt.
"""

"""
    Buenas prácticas para depurar y manejar errores

    a) Usa print() estratégicamente para depurar.
    b) Prueba funciones con valores simples y controlados.
    c) Comenta partes del código para aislar el problema.
    d) Especifica siempre las excepciones más precisas primero.
    e) Tómate descansos para ver tu código con “ojos nuevos”.
    f) Si puedes, pide feedback a otra persona.
"""

# Ejercicios:

# Pregunta 1: ¿Cuál es la salida del siguiente programa si el usuario ingresa un 0?

try:
    value = int(input("Ingresa un número entero: "))
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...") # Imprime: entrada errónea, al dividir 0/0
except:
    print("¡Buuuu!")

"""
    Observaciones:

    El código intenta dividir value / value.
    Si el usuario ingresa 0, el programa hace 0 / 0, lo cual lanza una excepción ZeroDivisionError.
    El except ZeroDivisionError captura correctamente ese error.
"""

# Pregunta 2: ¿Cuál es la salida del siguiente programa si el usuario ingresa un 0?

value = input("Ingresa un número entero: ")
print(10/value) # Se lanza: una excepcion de tipo, TypeError

"""
Problema:

input() devuelve una cadena (str), por lo tanto, 10 / value es 10 / '0', lo que 
provoca un TypeError.
"""
