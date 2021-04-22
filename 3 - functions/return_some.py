from random import randint
def par_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

print(par_impar(10))

resultado = par_impar(randint(1,10))
print(resultado)