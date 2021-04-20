from sys import exit



while(True):
    response = input("¿Que quieres hacer?: ")
    print(f'Elejiste {response}')
    if response == "exit":
        exit() #Termina el programa
    else:
        print("en bucle")

print("Afuera del  bucle") #Como exit() finaliza el programa esto nunca se imprime
