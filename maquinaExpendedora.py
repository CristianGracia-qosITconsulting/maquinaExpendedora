import time

# Se le pasa un minimo y un maximo e itera un bucle infinito hasta que el usuario introduzca un numero en ese rango. Devuelve el numero.
def opcion_user(min, max):
    bucle = True
    while True:
        try:
            n = int(input())
            if n >= min and n <= max:
                return n
            else:
                print("Ha ocurrido un error, intentelo de nuevo.")
        except Exception:
            print("Ha ocurrido un error, intentelo de nuevo.")

# Muestra la lista de golosinas con su codigo, nombre y precio.
def ver_golosinas():
    print(f"{"COD":7}{"NOMBRE":20} {"PRECIO"}")
    for i, (golosinas, precios) in enumerate(productos.items(), start=0):
        print(f"{str(i):7} {golosinas:20} {precios}€")
    
    time.sleep(3)

# Pide el codigo de una golosina y delvuelve su precio
def pedir_golosina():
    print("Introduce el código del producto:")
    cod = opcion_user(0,len(productos)-1)

    if stock[cod] == 0:
        print("No quedan mas unidades de este producto.")
        return 0

    ventas_por_producto[cod]+=1
    stock[cod]-=1

    print(f"Ha comprado: {nombres[cod]}")
    return precios[cod]

# Pide una contraseña, si esta es correcta pide el codigo del producto a rellenar, despues pide la cantidad de unidades a añadir
def rellenar_stock():
    contrasena = "123"
    intentoUser = input("Introduce la contraseña:")

    if(contrasena != intentoUser):
        print("Contraseña incorrecta.")
        return
    
    print("Introduce el codigo del producto:")
    cod = opcion_user(0,len(productos)-1)

    print(f"Has seleccionado: {nombres[cod]}")
    print("Introduce las unidades que quieras introducir(100 maximo):")
    unidades = opcion_user(1,100)

    stock[cod] += unidades
    print(f"Este producto ahora tiene: {stock[cod]} unidades")

# Imprime una lista de los productos vendidos, lo recaudado con cada uno de ellos y el total.
def informe_ventas():
    if not max(ventas_por_producto) == 0:
        print(f"{"Nombre":18} {"Vendidos":10} Total")
    
    for i in range(len(nombres)):        
        if ventas_por_producto[i] > 0:
            print(f"{nombres[i]:18} {str(ventas_por_producto[i]):10} {precios[i]*ventas_por_producto[i]}\n")
    
    print("Total recaudado: " + str(ventas_totales))


#dict de los productos y su precio
productos = {
                "Kit-Kat" : 1.5,
                "Pipas grefusa" : 1.2,
                "Bolsa hariboo" : 1,
                "Chicles de fresa": 0.8,
                "Lacasitos": 1.4,
                "Palotes": 0.9,
                "Kinder bueno": 2
            }
#listas sacadas de valores y claves del diccionario productos
precios = list(productos.values())
nombres = list(productos.keys())


# List de la cantidad inicial de cada uno de los productos existentes.
stock = [5] * len(productos)
ventas_por_producto = [0] * len(productos)
ventas_totales = int(0)

while True:
    print("\n1. Comprar golosina\n2. Ver golosinas\n3. Rellenar stock\n4. Salir")
    ind = opcion_user(1,4)
    
    if ind == 1:
        ventas_totales += pedir_golosina()
    elif ind == 2:
        ver_golosinas()
    elif ind == 3:
        rellenar_stock()
    elif ind == 4:
        informe_ventas()
        print("Saliendo...")
        break
# crear rama y leer fichero








