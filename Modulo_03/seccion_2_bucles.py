# pregunta 1
for i in range(0, 11):
    if i % 2 == 1: 
        print(i) # imprime numeros impares

# pregunta 2
contador:int = 1
while contador <= 10:
    if contador % 2 == 1:
        print(contador) # imprime numeros impares
    contador += 1

# pregunta 3
frase:str = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    frase += ch

print(frase)

# otra forma de hacerlo
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# pregunta 4
digitos_factorizados:str = ""  
for digit in "0165031806510":
    if digit == "0":
        digit = "x"
        digitos_factorizados += digit
        continue
    digitos_factorizados += digit

print(f"\n{digitos_factorizados}")

# otra forma 
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")


# pregunta 5
n = 3
 
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n) # imprime 3 2 0


# pregunta 6

n = range(4)

for num in n:
    print(num -1)
else: 
    print(num) # imprime -1 0 1 2 3


# pregunta 7
for i in range(0, 6, 3):
    print(i) # imprime 0 y 3