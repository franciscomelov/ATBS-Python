from random import randint

secret_number = randint(1,20)

#print(f'Secret number: {secret_number}')

print("Guess the number beetwen 1-20")

# Se puede cambiar el numero de intentos
for counter in range(1,7): #6 iteraciones
    user_guess = int(input("your guess: "))

    if user_guess < secret_number:
        print("mayor")
    elif user_guess > secret_number:
        print("menor")

    else:
        print(f'Correcto, en {counter} turnos')
        break


