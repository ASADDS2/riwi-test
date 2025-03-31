#Entrada.
 #Empezamos por ingresar el nombre del producto.

def obtener_dato_producto():
 return input ("ingresa el nombre del producto => ")


#Procesamiento.
#Definimos la variable precio, procedemos a ingresarla y al mismo tiempo validamos que sea un numero positivo.
def obtener_precio_unitario():
    while True:
        try:
            precio = float(input("Ingrese el precio unitario del producto => "))
            if precio > 0:
                return precio
            else:
                print("El precio debe ser un número positivo, por favor ingreselo nuevamente")
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")
            
#Definimos la variable cantidad de productos, procedemos a ingresarla y al mismo tiempo validamos que esta sea un numero positivo.
def obtener_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos adquiridos => "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")
            
#Definimos la variable descuento, procedemos a ingresarla y al mismo tiempo validamos que esta sea un numero positivo.
def obtener_descuento():
    while True:
        try:
            descuento = float(input("Ingrese el porcentaje de descuento (0-100) =>"))
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, ingrese un número válido para el descuento.")
            
#Operaciones de las funciones del programa.
def calcular_costo_total(precio_unitario, cantidad, descuento):
    costo_sin_descuento = precio_unitario * cantidad
    costo_con_descuento = costo_sin_descuento * (1 - descuento / 100)
    return costo_sin_descuento, costo_con_descuento

#Mostramos los resultados .
def mostrar_resultado(nombre_producto, costo_sin_descuento, costo_con_descuento): 
  
    print("\Resumen de la compra:")
    print(f"Producto: {nombre_producto}")
    print(f"Costo sin descuento: ${costo_sin_descuento:.2f}")
    print(f"Costo con descuento: ${costo_con_descuento:.2f}")
    
    
    
#Salida.
nombre_producto = obtener_dato_producto()
precio_unitario = obtener_precio_unitario()
cantidad = obtener_cantidad()
descuento = obtener_descuento()

costo_sin_descuento, costo_con_descuento = calcular_costo_total(precio_unitario, cantidad, descuento)

mostrar_resultado(nombre_producto, costo_sin_descuento, costo_con_descuento)