temperaturas_semana = [
    [-1, 16],  # Lunes
    [4,  17],  # Martes
    [4,  19],  # Miércoles
    [7,  23],  # Jueves
    [10, 26],  # Viernes
    [9,  24],  # Sábado
    [8,  22]   # Domingo
]
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = [0,0]
contador_dias = 0

for dia in temperaturas_semana:
    print(dia)
    suma_minimas += dia[0]
    suma_maximas += dia[1]
    amplitud = dia[1] - dia[0]

    if amplitud > mayor_amplitud[1]:
        mayor_amplitud = [contador_dias, amplitud]

    contador_dias += 1

promedio_minimas = suma_minimas / 7
promedio_maximas = suma_maximas / 7

print(f"Promedio de temperaturas minimas = {promedio_minimas}")
print(f"Promedio de temperaturas maximas: {promedio_maximas}")

print(f"Mayor amplitud termica: {mayor_amplitud[1]}°")
match mayor_amplitud[0]:
    case 0:
        print("Dia: Lunes")
    case 1:
            print("Dia: Martes")
    case 2:
            print("Dia: Miercoles")
    case 3:
            print("Dia: Jueves")
    case 4:
            print("Dia: Viernes")
    case 5:
            print("Dia: Sabado")
    case 6:
            print("Dia: Domingo")
