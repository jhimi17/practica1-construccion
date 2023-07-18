


#3. numero entero diferente de 0 y muestre sus divisores..
numero = 0
while numero == 0:
    try:
        numero = int(input("Ingrese un número diferente de cero: "))
        if numero == 0:
            print("El número debe ser diferente de cero. Inténtelo nuevamente.")
    except ValueError:
        print("Error: Debe ingresar un número entero. Inténtelo nuevamente.")

divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print("Los divisores de", numero, "son:", divisores)