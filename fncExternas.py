turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Chile", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
"004": ["Jessica Davis", "Estados Unidos","15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-03-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"],}

def turistas_por_pais(pais):
    unaLista=[]
    encontrado = False
    for i,j in turistas.items():
        if pais == j[1]:
            unaLista.append(j[0])
            encontrado = True
    
    if not encontrado:
        print("No hay turistas de ese pais")
    else:    
        print(unaLista)
    
def turistas_por_mes(mes):
    contador = 0
    contadorC = 0
    for i,j in turistas.items():
        separacion= j[2].split("-")
        
        if int(separacion[1]) == mes:
            contador+=1
            if j[1] == "Chile":
                contadorC+=1
    
    if contadorC > 0:       
        porcentaje = contadorC/contador*100
    else:
        porcentaje = 0
    
    return porcentaje


def eliminar_turista():
    nombre = input("Ingrese nombre del turista a eliminar ")
    encontrado = False
    for i,j in turistas.items():
        if nombre.upper() == j[0].upper():
            encontrado = True
            del turistas[i]
            print("Turiste eliminado con exito")
            break
       
    if not encontrado:
        print("Turista no encontrado. No se pudo eliminar") 
    
   
       
    
    
            
       

        