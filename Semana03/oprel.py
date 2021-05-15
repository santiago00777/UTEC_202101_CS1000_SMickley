#Ejercicio 1
a = input()
b = input()
a = int(a)
b = int(b)

rp = ((a!=b) or (a>=b)) and (a%b==1)
rp = rp*1
print(rp)
