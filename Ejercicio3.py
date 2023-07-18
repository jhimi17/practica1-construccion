
#3. numero entero diferente de 0 y muestre sus divisores..
numero = int(input("Ingrese un número entero diferente de 0: "))

# Validar que el número sea diferente de cero
while numero == 0 :
    numero = int(input("El número debe ser diferente de 0. Ingrese otro número: "))

divisores = []

# Encontrar los divisores del número

for i in range(1, abs(numero) + 1):
    if numero % i == 0:
        divisores.append(i)

# Mostrar los divisores encontrados
print("Los divisores de", numero, "son:", divisores)