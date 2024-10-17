print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
precios_frutas = { #diccionarios con las frutas
    'mango': 10.5,
    'coco': 12,
    'uvas': 15.5,
    'fresa': 13.2,
    'arandanos': 20.5
}
print(" ")
fruta = input("¿Qué fruta quieres comprar? ").lower() #variable y pregunta 
kilos = float(input("¿Cuántos kilos quieres comprar? "))#variable y pregunta 

# Ver si la fruta está en el diccionario
if fruta in precios_frutas:#si si esta 
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio total de {kilos} kilos de {fruta} es: ${precio_total:.2f}")
else:#si no esta 
    print(f"perdon, la fruta '{fruta}' no está en el diccionario.")
