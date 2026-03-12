"""
var
op com ver
condições

loops - ?

"""
"""
# while

contador = 0

while contador <= 10:
    print(contador)
    contador += 1

# faça um programa que mostre a tabuada do 2

# 1 ao 10

"""
# 2 x 1 = 2
# 2 x 2 = 4
# ....
# 2 x 10 = 20
"""
print("-----------------")

tab = 2
contador = 1

while contador <= 10:
    print(f"{tab} x {contador:2} = {tab * contador}")
    contador += 1

# calcule o fatorial de n, o valor n deve ser pedido ao utilizador
"""

n = int(input("num: "))
fatorial = n
aux = n  # so para não destruir o n
# n! = n * n-1 * n-2 * ... * 1
# n! = 1 * 2 * 3 * ... * n-1 * n

# 5! = 5 * 4 * 3 * 2 * 1 = 120

# 3! = 3 * 2 * 1
# 3! = 6 * 1
# 3! = 6

# 4! = 4 * 3 * 2 * 1
# 4! = 12 * 2 * 1
# 4! = 24 * 1
# 4! = 24
"""
while aux > 1:
    aux -= 1
    print(f"{fatorial} x {aux} = {fatorial * aux}")
    fatorial = fatorial * aux

print(f"{n}! = {fatorial} ")

"""
print("-----" * 5)
contador = 100

while contador > 0:
    print(contador)
    if contador == 80:  # o valor do contador for par entra
        break  # o while termina

    contador -= 1

# crie um programa que leia no max 100 num,
# mas se o utilizador inserir um valor negativo termine o programa

# ler no max 100 num

# se num < 0 -> parar

print("-------")

max_num = 10
curr = 1

while curr <= max_num:

    n = int(input(f"num {curr}: "))

    if n < 0:
        break
    curr += 1
