# contador = 0
# suma = 0
# numero_maximo = float (input("Introduce el numero maximo a sumar: "))
# while contador < numero_maximo:
#     suma += contador
#     contador += 5
# print(f"La suma es: {suma}")

# tabla = float(input("Introduce la tabla de multiplicar que quieres ver: "))
# inicio = 1

# while inicio <= 10:
#     resultado = tabla * inicio 
#     print(tabla, "*",inicio, "=",resultado)
#     inicio += 1

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

numero_inicial = float(input("Introduce tu numero inicial: "))
numero_final = float(input("Ingresa tu numero final: "))

cantidad = 0 
while numero_inicial < numero_final:
    if numero_inicial % 2 == 0:
        print(numero_inicial)
        cantidad += 1
    numero_inicial += 1
print("Hay", cantidad,"numeros pares")