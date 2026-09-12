lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
nombre_operador = ""

while not nombre_operador.isalpha:
    nombre_operador = input("Nombre Operador: ")

menu = ""
while menu != "5":
    print('''
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema''')

    match menu:
        case "1":
            nombre_paciente = ""
            dia = input("1->Lunes, 2->Martes")
            while not nombre_paciente.isalpha():
                nombre_paciente = input("Nombre del paciente: ")
            if dia == "1":
                
            
            
