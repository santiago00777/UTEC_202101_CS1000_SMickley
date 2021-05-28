num = 42

base = 2
# Primera división
residuo = num % base
cociente = num // base
bit1 = residuo

# Segunda división
residuo = cociente % base
cociente = cociente // base
bit2 = residuo

# Tercera división
residuo = cociente % base
cociente = cociente // base
bit3 = residuo

# Cuarta división
residuo = cociente % base
cociente = cociente // base
bit4 = residuo

# Quinta división
residuo = cociente % base
cociente = cociente // base
bit5 = residuo

# Sexto división
residuo = cociente % base
cociente = cociente // base
bit6 = residuo



print("{}={}{}{}{}{}{}".format(num,bit6,bit5,bit4,bit3,bit2,bit1))

