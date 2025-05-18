# 01 ¿Cuál es el resultado del siguiente fragmento de código?

x = 5
y = 10
z = 8
 
print(x > y) # imprime False
print(y > z) # imprime True

# 02 ¿Cuál es el resultado del siguiente fragmento de código?

x, y, z = 5, 10, 8
 
print(x > z) # imprime False
print((y - 5) == x) # imprime True

# 03 ¿Cuál es el resultado del siguiente fragmento de código?

x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z) # imprime True
print((y - 5) == x) # imprime False

# 04 ¿Cuál es el resultado del siguiente fragmento de código?

x = 10
 
if x == 10:
    print(x == 10) # imprime True
if x > 5:
    print(x > 5) # imprime True
if x < 10:
    print(x < 10) 
else:
    print("else") # imprime else

# 05 ¿Cuál es el resultado del siguiente fragmento de código?

x = "1"
 
if x == 1:
    print("one") 
elif x == "1": 
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four") # imprime four
if int(x) == 1:
    print("five") # imprime five
else:
    print("six")

# 06 ¿Cuál es el resultado del siguiente fragmento de código?

x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one") # imprime one
if y == int(z):
    print("two") # imprime two
elif x == y:
    print("three")
else:
    print("four")
