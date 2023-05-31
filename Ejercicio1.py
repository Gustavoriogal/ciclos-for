CANT_VALORES = 5

suma = 0
for x in range(1, CANT_VALORES + 1):
    print("Ingrese el ", x, "º valor: ", sep = "", end = "")
    suma += int(input())
print("\n\nLa suma de los", CANT_VALORES, "valores ingresados es", suma)