# Ejercicio 01

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst) # Imprime [6, 2, 3, 4, 5, 1]


# Ejercicio 02

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst: 
    add += number
    lst_2.append(add)

print(lst_2) # Imprime [1, 3, 6, 10, 15]


# Ejercicio 03

lst = []
# Elimina la variable 'lst' del ámbito (scope). 
# Al no indicar un índice (como lst[0]), se borra la referencia completa a la lista, 
# por lo tanto, 'lst' deja de existir y sus elementos (si los hubiera) también se eliminan 
# si no hay otras referencias a ellos.
del lst 
print(lst) # Imprime ERROR que lst no esta definida