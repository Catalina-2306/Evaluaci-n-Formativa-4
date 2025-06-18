import fncExternas as fnc

opc=0
while opc < 1 or opc > 4:
    print('*** MENU PRINCIPAL ***')
    print("""
    1.- Turistas por país.
    2.- Turistas por mes. 
    3.- Eliminar turista.
    4.- Salir""")   
    opc = int(input('Ingrese su opción: '))
                
    if opc == 1:
        pais=input("Ingrese pais a buscar: ")
        fnc.turistas_por_pais(pais)
    elif opc == 2:
        mes=0
        while mes < 1 or mes > 12:
            try:
                mes=int(input("Ingrese mes a buscar: "))
                if mes < 1 or mes > 12:
                    print("Debe ingresar un valor entre 1 y 12. Intentelo nuevamente")
                else:
                    porcentaje = fnc.turistas_por_mes(mes)
                    print("El numero de turistas equivale al ",round(porcentaje,1)," % del total.")
                    break    
            except:
                print("Debe ingresar un valor numerico")
    
    elif opc == 3:
        fnc.eliminar_turista()
    
    elif opc == 4:
        print("Programa terminado...")
    else:
        print("Debe ingresar una opcion valida!! ")
        
    