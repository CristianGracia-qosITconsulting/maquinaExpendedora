import time

# Le envias por parametro un array de Strings y te lo devuelve convertido a int
def str_to_int(arr):
    arr_int = list()
    for i in range(len(arr)):
        arr_int.append(int(arr[i]))
    
    return arr_int

def str_to_float(arr):
    arr_float = list()
    for i in range(len(arr)):
        arr_float.append(float(arr[i]))
    
    return arr_float

#lee el fichero, guarda los datos en listas y los devuelve.
def leer_fichero():
    
    with open("fichero.txt") as f:
        cantidad = int(f.readline())
        productos, precios, stock = [], [], []

        for i in range(cantidad):
            productos.append(f.readline().rstrip().split(","))
        for i in range(cantidad):
            precios.append(str_to_float(f.readline().rstrip().split(",")))
        for i in range(cantidad):
            stock.append(str_to_int(f.readline().rstrip().split(",")))
            
        
        return productos, precios,stock

#Pedir código del producto
def pedir_codigo_producto():
    bucle = True
    while bucle:
        try:
            cod = int(input())

            if cod > 99: 
                print("Error, intentelo de nuevo.")
                blucle = True
            else:
                f = int(cod/10)
                c = int(cod%10) 
                print(f,c)
                stock[f][c] = stock[f][c] #compruebo si esa posición existe
                bucle = False   
        
        except:
            bucle = True
            print("Error, intentelo de nuevo.")

    return f,c
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
    for i in range(len(productos)):
        for j in range(len(productos[i])):
            print(f"{str(i)+str(j):7} {productos[i][j]:20} {precios[i][j]}€")
    
    time.sleep(3)

# Pide el codigo de una golosina y delvuelve su precio
def pedir_golosina():
    print("Introduce el código del producto:")
    f, c = pedir_codigo_producto()

    if stock[f][c] == 0:
        print("No quedan mas unidades de este producto.")
        return 0

    ventas_por_producto[f][c]+=1
    stock[f][c]-=1

    print(f"Ha comprado: {productos[f][c]}")
    return precios[f][c]

# Pide una contraseña, si esta es correcta pide el codigo del producto a rellenar, despues pide la cantidad de unidades a añadir
def rellenar_stock():
    contrasena = "123"
    intentoUser = input("Introduce la contraseña:")

    if(contrasena != intentoUser):
        print("Contraseña incorrecta.")
        return
    
    print("Introduce el codigo del producto:")
    f,c = pedir_codigo_producto()

    print(f"Has seleccionado: {productos[f][c]}")
    print("Introduce las unidades que quieras introducir(100 maximo):")
    unidades = opcion_user(1,100)

    stock[f][c] += unidades
    print(f"Este producto ahora tiene: {stock[f][c]} unidades")

# Imprime una lista de los productos vendidos, lo recaudado con cada uno de ellos y el total.
def informe_ventas():

    for i in range(len(productos)):
        for j in range(len(productos[i])):     
            if ventas_por_producto[i][j] > 0:
                print(f"{productos[i][j]:18} {str(ventas_por_producto[i][j]):10} {precios[i][j]*ventas_por_producto[i][j]}\n")
    
    print("Total recaudado: " + str(ventas_totales))

#listas sacadas del fichero
productos, precios, stock = leer_fichero()

# List de la cantidad inicial de cada uno de los productos existentes.
print(len(productos))
ventas_por_producto = lista = [[0] * 4 for _ in range(4)]
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
print(ventas_por_producto)
print(productos)
print(precios)
print(stock)