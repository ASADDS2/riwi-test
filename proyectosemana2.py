while True:
    try:
        calificacion = float(input("Ingrese su calificación (0-100): "))
        if 0 <= calificacion <= 100:
            break
        else:
            print("Error: La calificación debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

if calificacion >= 80:
    print("Has aprobado de manera sobresaliente")
elif calificacion >= 60:
    print("Has aprobado")
elif calificacion >= 30:
    print("Has reprobado")
else:
    print("Has reprobado estrepitosamente")

while True:
    respuesta = input("¿Quiere ingresar una lista de calificaciones? (Si/No): ").lower()
    if respuesta == "si":
        try:
            calificaciones_str = input("Ingrese calificaciones separadas por comas: ").split(",")
            calificaciones = []
            calificaciones_invalidas = False
            for calificacion_str in calificaciones_str:
                calificacion_float = float(calificacion_str)
                if 0 <= calificacion_float <= 100:
                    calificaciones.append(calificacion_float)
                else:
                    calificaciones_invalidas = True
                    break
            if calificaciones_invalidas:
                print("Error: Todas las calificaciones deben estar entre 0 y 100.")
            else:
                promedio = sum(calificaciones) / len(calificaciones)
                print(f"Promedio: {promedio:.2f}")

                valor_comparacion = float(input("Ingrese valor para comparar calificaciones: "))
                mayores = sum(1 for i in calificaciones if i > valor_comparacion)
                print(f"Calificaciones mayores que {valor_comparacion}: {mayores}")

                valor_busqueda = float(input("Ingrese calificación a buscar: "))
                conteo = calificaciones.count(valor_busqueda)
                print(f"La calificación {valor_busqueda} aparece {conteo} veces.")
                break
        except ValueError:
            print("Error: Ingrese números válidos separados por comas.")
    elif respuesta == "no":
        break
    else:
        print("Respuesta inválida. Responda 'Si' o 'No' ")
