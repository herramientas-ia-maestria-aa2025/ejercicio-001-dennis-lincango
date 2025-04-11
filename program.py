archivo = open("informacion.txt", "r", encoding="utf-8")
lineas = archivo.readlines()
archivo.close()

print(f"\nInformación: {lineas[0]}")
for i, linea in enumerate(lineas[1:], start=1):
    # Ejercicio 1
    # print(f"Persona {i}: {linea.strip()} ")

    # Ejercicio 2
    # campos = linea.strip().split(';')
    # apellido = campos[1]
    # if apellido.startswith('B'):
    #     print(f"Persona {i}: {linea.strip()}")

    # Ejercicio 3
    campos = linea.strip().split(';')
    for campo in campos:
        if  campo[-4:] == '.org':
            print(f"Persona {i}: {linea.strip()}")
            break
