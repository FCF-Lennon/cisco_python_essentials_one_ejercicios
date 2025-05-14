# ordenando listas con el ordenamiento de burbuja

my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

# usando el metodo sort() de las listas para ordenarlas

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# Ejercicio 01

lst = ["D", "F", "A", "Z", "H"]
lst.sort()
print(lst) # imprime ["A", "D", "F", "H", "Z"]

# Ejercicio 02

a = 3
b = 1
c = 2

lst = [a, b, c]
lst.sort()
print(lst) # imprime los numeros ordenados de forma ascendente


# Ejercicio 03

a = "A"
b = "B"
c = "C"
d = " "
 
lst = [a, b, c, d]
lst.reverse()
 
print(lst) # Imprime [" ", "C", "B", "A"]
 