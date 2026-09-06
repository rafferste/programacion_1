USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"
usuario = ""
clave = ""
contador = 0
    
while (usuario != USUARIO_CORRECTO or clave != CLAVE_CORRECTA) and contador < 3:
    print(f"Intento {contador+1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if (usuario != USUARIO_CORRECTO or clave != CLAVE_CORRECTA):
        print("Error: Credenciales inválidas")
        contador += 1
    else:
        print("Acceso concedido:")

if contador == 3:
    print("Cuenta bloqueada")
else:
    menu = ""
    while menu != "4":
        print('''
1. Ver estado de inscripción
2. Cambiar clave
3. Mostrar mensaje motivacional
4. Salir''')
        menu = input("Elija una opcio: ")

        match menu:
            case "1":
                print("---Inscripto---")

            case "2":
                clave_nueva = input("Clave nueva: ")
                confirmar_clave = input("Repita la clave: ")

                while clave_nueva != confirmar_clave:
                    print("Error: Las claves no coinciden!")
                    clave_nueva = input("Clave nueva: ")
                    confirmar_clave = input("Repita la clave: ")
                
                CLAVE_CORRECTA = clave_nueva

            case "3":
                print("Un programador de computadoras es un creador de universos para los cuales él es el único legislador... Ningún dramaturgo, ningún director de escena, ningún maestro constructor, se enfrentó jamás a tal falta de limitaciones")