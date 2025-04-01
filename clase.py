print("Bienvenido a la calculadora de grasa corporal")
peso = float(input("Por favor ingrese su peso: "))
estatura = float (input ("Por favor ingrese su estatura en metros: "))
indice_de_grasa_corporal = peso / estatura ** 2
print (f"Tu indice de grasa corporal es {indice_de_grasa_corporal}")