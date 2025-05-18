# 01 un operador que puede verificar si dos valores son iguales se codifica como:
# Respuesta ==

# 02 el valor asignado finalmente a x es igual a:

x = 1
x = x == x

print(x) # imprime True

# 03 ¿Cuántos * enviará el siguiente fragmento de código a la consola?
i = 0
while i <= 3 :
    i += 2
    print("*") # Imprime 2

# 04 ¿Cuántos (*) enviará el siguiente fragmento de código a la consola?

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*") # imprime solo 1


# 05 ¿Cuántos (#) enviará el siguiente fragmento de código a la consola

for i in range(1):
    print("#")
else:
    print("#") # imprime solo 2

# 06 ¿Cuántos (#) enviará el siguiente fragmento de código a la consola?

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#") # imprime 3

# 07 ¿Cuántos (#) enviará el siguiente fragmento de código a la consola?

var = 1
while var < 10:
    print("#") # imprime 4
    var = var << 1

# 08 ¿Qué valor será asignado a la variable x?

z = 10
y = 0
x = y < z and z > y or y > z and z < y

print(x) # imprime True

# 09 ¿Cuál es la output del siguiente fragmento de código?

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e) # imprime 2

# 10 ¿Cuál es la output del siguiente fragmento de código?

my_list = [3, 1, -2]
print(my_list[my_list[-1]]) # imprime 1

# 11 ¿Cuál es la output del siguiente fragmento de código?

my_list = [1, 2, 3, 4]
print(my_list[-3:-2]) # imprime [2]

# 12 ¿que hace la segunda asignación?

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0] # invierte la lista

# 13 Después de la ejecución del siguiente fragmento de código, 
# la suma de todos los elementos vals será igual a:

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]

print(sum(vals)) # imprime 4

# 14 Observa el código, y selecciona las sentencias verdaderas: (Selecciona dos respuestas)

nums = [1, 2, 3]
vals = nums
del vals[1:2]

"""Alternativas:

    a) nums y vals se refieren a la misma lista / respuesta 
    b) nums es replicada y asignada a vals
    c) nums y vals son de la misma longitud / respuesta
    d) nums es más larga que vals
"""

# 15 ¿Cuáles de los siguientes enunciados son verdaderos? (Selecciona dos respuestas)

nums = [1, 2, 3]
vals = nums[-1:-2]

"""Alternativas:

    a) nums es más larga que vals / respuesta 
    b) nums y vals son dos listas diferentes / respuesta
    c) nums y vals son de la misma longitud
    d) vals es más larga que nums
"""

# 16 ¿Cuál es la output del siguiente fragmento de código?

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2) # imprime [3, 2, 1]

# 17 ¿Cuál es la output del siguiente fragmento de código?

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list) # imprime [1, 1, 1, 1, 2, 3]

# 18 ¿Cuántos elementos contiene la lista my_list?

my_list = [i for i in range(-1, 2)]

print(len(my_list)) # imprime 3

# 19 ¿Cuál es la output del siguiente fragmento de código?

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s) # imprime 6

# 20 ¿Cuál es la output del siguiente fragmento de código?

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0]) # imprime error index fuera del rango



















