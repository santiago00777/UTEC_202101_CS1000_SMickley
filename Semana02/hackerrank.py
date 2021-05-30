#Ejercicio 1:
a = input()
b = input()
a = int(a)
b = int(b)

rp = ((a!=b) or (a>=b)) and (a%b==1)
rp = rp*1
print(rp)

#Ejercicio 2:

a = input()
b = input()
a = int(a)
b = int(b)

rp = not(a == b or a <= b) and ((a%b)!=2)
rp = rp*1
print(rp)

#Ejercicio 3:

a = input()
b = input()
a = int(a)
b = int(b)



rp = (a != b**2) and (a/b == 1)
rp = rp*1
print(rp)

# Ejercicio 4:
a = input()
b = input()
a = float(a)
b = float(b)


rp = ((b == round(a,2)) or (a*b > 10))
rp = rp*1
print(rp)

# Ejercicio 5:

import math

a = input()
b = input()
a = float(a)
b = float(b)

rp = not((math.sqrt(a**2+b**2)) == (2*a - b))

rp = rp*1
print(rp)

# Ejercicio 6:

import math

a = input()
b = input()
a = float(a)
b = float(b)



rp = (math.trunc(a*100)/100 == b)
rp = rp*1
print(rp)

# Ejercicio 7:

a = input()
b = input()
a = int(a)
b = int(b)

problema = bin(round(a, 3)) == bin(round(b, 3))

problema = problema*1

print(problema)

# Ejercicio 8:

a = input("")
b = input("")


rp = (a != b) and len(a) == len(b)

rp = rp*1
print(rp)

# Ejercicio 9:

a = input()
b = input()
a = float(a)
b = float(b)

rp = (round(a, 2) == round(b, 2))

rp = rp*1
print(rp)

# Ejercicio 10:

a = input("")
b = input("")
c = input("")

rp = (len(a) > len(b)) or (len(b) > len(c) and len(a) > len(c))

rp = rp*1
print(rp)




