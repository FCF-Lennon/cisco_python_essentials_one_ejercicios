# slicing  o rebanadas en listas 

# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
# segmenta [inicio:fin-1] quiere decir que el 
# ultimo indice no se cuenta en el segmento
new_list = my_list[1:3] 
print(new_list) # Imprime [8, 6] y deja afura al 4 creando una nueva lista con esos elementos

# Instrucción - del

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) # Imprime [10, 4, 2]


"""
Escenario:
Imagina una lista - no muy larga ni muy complicada, solo una lista simple 
que contiene algunos números enteros. Algunos de estos números pueden estar 
repetidos, y esta es la clave. No queremos ninguna repetición. 
Queremos que sean eliminados.

Tu tarea es escribir un programa que elimine todas las repeticiones de números 
de la lista. El objetivo es tener una lista en la que todos los números aparezcan 
no más de una vez.

Nota: Asume que la lista original está ya dentro del código - no tienes que ingresarla 
desde el teclado. Por supuesto, puedes mejorar el código y agregar una parte que pueda 
llevar a cabo una conversación con el usuario y obtener todos los datos.

Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo 
temporal - no necesitas actualizar la lista actual.

"""

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for number in my_list:
    if number not in new_list:
        new_list.append(number)
print("La lista con elementos unicos: ")
print(new_list)


# Ejercicio 01

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[0]
 
print(list_1) # Imprime solo ["C"]


# Ejercicio 02

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2  # Esto elimina la referencia a la lista, no la lista

print(list_3)  # Imprime ["B", "C"]


# Ejercicio 03

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[:] # Elimina todos los elementos que estan dentro de la lista con slicing "Rebanar o rebanada"
 
print(list_3) # Imprime una lista vacia []


# Ejercicio 04

List_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3) # Imprime ["A", "B", "C"]


# Ejercicio 05

my_list = [1, 2, "in", True, "ABC"]
 
""" 
    print(1 ??? my_list)  # output True
    print("A" ??? my_list)  # output True
    print(3 ??? my_list)  # output True
    print(False ??? my_list)  # output False 
"""

print(1 in my_list)
print("A" not in my_list)
print(3 not in my_list)
print(False in my_list)