def convertir_base(numero, base):
  # Definimos la cadena digitos para evitar ambiguedades en caso nuestra base fuera hexadecimal
  digitos = "0123456789ABCDEF"
  # Cadena de texto donde almacenaremos el resultado final
  resultado = ""
  # Hacemos divisiones sucesivas hasta que el cociente sea 0
  while numero // base != 0:
    # Calculamos el residuo utilizando el operador % (módulo)
    residuo = numero % base
    # Concatenamos los residuos de las divisiones a nuestro resultado,pues vienen a ser los dígitos de nuestro número convertido
    resultado = resultado + digitos[residuo] # accedemos a la letra que esta en la poscición indicada por el residuo en la variable dígitos
    # Realizamos la divisón respectiva, luego de haber sacado el residuo
    numero = numero // base
  # Añadimos el cociente que queda al realizar la última división, pues este representa el primer dígito de nuestro número convertido
  resultado = resultado + digitos[numero] # igual  que en la linea 14
  # Invertimos la cadena de texto resultado utilizando una propiedad de los iterables
  resultado = resultado[::-1]
  # Imprimimos el resultado
  print(resultado)

# Ejercicio 1
convertir_base(13, 8)

# Ejercicio 2
convertir_base(18, 8)

# Ejercicio 3
convertir_base(48, 16)

#Ejercicio 4
convertir_base(99, 16)

#Ejercicio 5
convertir_base(67, 16)

# Ejercicio 6
convertir_base(104, 2)

#Ejercicio 7
convertir_base(254, 2)

# Ejercicio 8
convertir_base(305, 16)

# Ejercicio 9
convertir_base(587, 8)

#Ejercico 10
convertir_base(788, 2)
