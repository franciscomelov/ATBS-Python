from random import randint
# opciones = 
# piedra pi  -  tijera ti  -  papel pa    .salir  s


ganados = 0
perdidos = 0
empates = 0

while(True):
    
#marcador
    print(f'gandos: {ganados}  -  empates: {empates}  -  perdidos: {perdidos}')
    print("*****************************************************")
#usuario opcion
    jugador = input("""
    [pi] Piedra
    [pa] Papel
    [ti] Tijera
    [s] Salir
    Escoje: """)

#salir
    if jugador == "s":
        break
    
#Maquina tiro
    maquina = randint(1,3)
    if maquina == 1: maquina = "pi"
    elif maquina == 2: maquina = "pa"
    else: maquina = "ti"

#Mjugada de jugador
    if jugador == "pi": print("Piedra VS",end="")
    elif jugador =="pa": print("Papel VS",end="")
    elif jugador == "ti": print("Tijera VS",end="")

#Mjugada de maquina
    if maquina == "pi": print(" Piedra")
    elif maquina =="pa": print(" Papel")
    elif maquina == "ti": print(" Tijera")

#Logica del juego
#empate
    if maquina == jugador:
        print("Empate")
        empates += 1
#Jugador gana
    elif jugador == "pi" and maquina == "ti":
        print("Ganaste")
        ganados += 1
    elif jugador == "pa" and maquina =="pi":
            print("Ganaste")
            ganados += 1
    elif jugador == "ti" and maquina == "pa":
            print("Ganaste")
            ganados += 1
    else:
        print("Perdiste")
        perdidos +=1
        #Ya no es necesario escribir las demas opciones
        #todos los casos donde gana o es empate estan escritos
        #la unica otra opcion seria perder
    print("*****************************************************")






