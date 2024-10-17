print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W") #nombre del programador
print(" ")
divisas = {"euro": "€", "dollar": "$", "yen": "¥"} #se ponen los nombres de las monedas
print(" ")
divisa_usuario = input("Ingresa una divisa (euro, dollar, yen): ") #sirve para ingresar  la divisa que el usuario quiere
print(" ")
if divisa_usuario in divisas:  # si la divisa que el usuario ingreso esta en el diccionario
    print(f"El símbolo de {divisa_usuario} es: {divisas[divisa_usuario]}")  #imprime el símbolo de la divisa
else:   # si la divisa que el usuario ingreso no esta en el diccionario
    print("La divisa no está en el diccionario.")   #imprime un mensaje de error
print(" ") 
