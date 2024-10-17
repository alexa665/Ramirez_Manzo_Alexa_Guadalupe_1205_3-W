print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")
print(" ")
informacion = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}
print(" ")
print(f"{informacion['nombre']} tiene {informacion['edad']} años,")
print(f"vive en {informacion['direccion']} ")
print(f"y su número de teléfono es {informacion['telefono']}.")
print(" ")
