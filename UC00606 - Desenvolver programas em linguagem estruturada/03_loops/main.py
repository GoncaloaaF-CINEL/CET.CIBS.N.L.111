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

n = 0  # int(input("num: "))
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

max_num = 0
curr = 1

while curr <= max_num:

    n = int(input(f"num {curr}: "))

    if n < 0:
        break
    curr += 1

"""

var
op var 
condiçoes 
    if
    elif
    else

loops
    while
    
---------------
    
"""

## range

range(5)  # 0, 1, 2, 3, 4 ->  range(n) -> todos os num int 0 e n-1
range(3)  # 0, 1, 2

range(2, 5)  # 2, 3, 4 ->  range(m, n) -> todos os num int m e n-1

range(10, 20, 2)  # 10, 12, 14, 16, 18 -> ->  range(m, n, s) -> todos os num int m e n-1 com um step de s

#  range(lb, ub, s) --> lb ate ub-1 com step s


# num int de 0 a 100 de 5 em 5

range(0, 20, 5)  # 0 até 20-1, mas de 5 em 5
# 0, 5, 10, 15


# crie um intervalo com todos os num de 20 a 45 com um step de 3
range(20, 45, 3)

# range(lb, ub, s) --> lb ate ub-1 com step s

# q num estão nos range
# range(3, 8, 2)  # 3, 5, 7
# range(3, 10, 3) # 3, 6, 9
# range(7, 10, 3) # 7

print("------------------")

for i in range(5):
    print(i)

print("------------------")
for i in range(3, 8, 2):
    print(i)

print("------------------")
for num in range(3, 8, 2):
    print(num)

# faça um programa que calcule a tabuada do N, onde o n e fornecido pelo utilizador, deve usar um for

tabuada = int(input("tabuada: "))

for i in range(10):
    aux = i + 1
    print(f"{tabuada} x {aux:2} = {aux * tabuada:2}")

print("--")
for i in range(1, 11):
    print(f"{tabuada} x {i:2} = {i * tabuada:2}")

print("--")

for i in range(2, 22, 2):
    n = i // 2
    print(f"2 x {n} = {i}")
print("--")
print("--")
# calcule o fatorial de n, o valor n deve ser pedido ao utilizador deve usar um for

# 3! = 3 * 2 * 1 <=> 1 * 2 * 3
# 3! = 6 * 1
# 3! = 6


# 4! = 4 * 3 * 2 * 1
# 4! = 12 * 2 * 1
# 4! = 24 * 1
# 4! = 24


n = 4

fact = n
for i in range(1, n):
    print(f"{fact} x {i:2} = {fact * i:2}")
    fact *= i

print(f"{n}! = {fact}")

print("--")

n = 4
fatorial = 1
for i in range(n, 1, -1):
    fatorial *= i

print(f"{n}! = {fatorial}")

######### Loops ###################


# faça um programa que peça ao utilizador números,
#   qd for introduzido um valor negativo deixa de pedir números

# while ou for ?

while True:
    n = int(input("inicio: "))
    if n < 0:
        break

n = 0
while n >= 0:
    n = int(input("inicio 2: "))
    print(f"o num digitado foi {n}")

while (n := int(input("inicio 3: "))) > 0:
    print(f"o num digitado foi {n}")

# faça um programa que peça até 100 números ao utilizador,
#   qd for introduzido um valor negativo deixa de pedir números

for i in range(1, int(11)):
    n = int(input(f"for {i} - digite um número: "))
    if n < 0:
        break
