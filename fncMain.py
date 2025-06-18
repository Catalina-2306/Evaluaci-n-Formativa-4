import fncExternas as fnc

turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
"004": ["Jessica Davis", "Estados Unidos","15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-10-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"],}

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
        
    