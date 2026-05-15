nome = "Gonçalo" # <- str
idade = 12 # <- int
altura = 1.5 # <- float

idade = "dez"  # <- str

media:float = 12.3
print(media)
print(type(media))


media = 34
print(media)
print(type(media))

media = "Dez"
print(media)

print(type(media))

print("-------------------------")

soma = 1 + 4
print(soma)

soma2 = soma - 2
print(soma2)


soma3 = 3 + 6.1
print(soma3)

div = 5 / 2
print(div)


mod = 5 % 2
print(mod)


mod = 5 // 2
print(mod)


soma_s = "1" + "4"
print(soma_s)

v1 = "1"
v2 = "2"
soma_s2 = f"{v1}{v2}"

"""
print("-1-" * 10)

n1 = float(input("Valor 1: "))
n2 = float(input("Valor 2: "))

soma = n1 + n2
print(f"soma 1: {soma}")


n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))

soma = n1 + n2
print(f"soma 2: {soma}")
"""

print("-" * 10)

# if
# elif
# else

idade = 10

if idade >= 18:     # se
    print("Adulto")
elif idade > 12:    #senão se
    print("teen")
else:               #senão
    print("kid")

print("-" * 10)

for i in range(1, 11):
    print(i)
    if i == 6:
        break





print("-" * 10)
for i in range(1, 20, 2):
    print(i)
    if i == 7:
        break



print("-" * 10)
for i in range(0, 20, 5):
    print(i)
    if i == 6:
        break


print("-" * 10)

i = 0
while i < 10:
    print(i)
    i += 3


"""
1 - faça uma programa em python que peça números ao utilizador ate ser inserido um valor negativo

1.2 - conte os números impar inseridos
1.3 - mostre apenas os par

1.4 - calcule a media dos impar
1.5 - indique o maior e o menor (sem usar listas)
"""

contador = 0
soma = 0

maior = None
menor = None

while True:
    n = int(input("Digite um numero: "))
    if n < 0:
        break

    if maior is None:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    if n % 2 == 0:
        print(n)
    else:
        soma += n
        contador += 1


# ver se o contador é 0
media = soma / contador
print(media)