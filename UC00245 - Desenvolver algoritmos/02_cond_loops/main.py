# condições - if

idade = 10

if idade >= 18:  # {
    print("linha 1")
    print("Adulto")
    print("linha 3")
# }
else:
    print("linha 1")
    print("não adulto")
    print("linha 3")

print("---------------------------")

"""
idade < 12 -> kid
idade > 12 e idade < 18 -> teen 
idade >= 18 -> adulto
"""

idade = 16

if idade >= 18:
    print("Adulto")

elif idade > 12:  # and idade < 18:
    print("teen")

else:
    print("kid")

print("---------------------------")
"""
crie uma app para calcular se um aluno esta aporvado (media >= 10), 
se vai a oral (media >= 8) ou se esta chumbado (media < 8)

"""
media = 34

if media >= 10:
    print("Aprovdo")

elif media >= 8:  # and idade < 18:
    print("Oral")

else:
    print("Chumbado")

# loops - while

print("---------------------------")
contador = 0

while contador < 20:
    print(f"Ola Mundo: {contador}")
    contador += 1

print("---------------------------")

"""
peça ao utilizador 5 números e calcule a media dos 5 números

"""

max_num = int(input(f"Digite o número de notas por aluno: "))  # total pedidos
num_pedidos = 0  # qts num já foram pedidos
sum_num = 0  # soma inicial

while num_pedidos < max_num:  # 0 1 2 3 4
    num_pedidos += 1
    num = int(input(f"Digite um nota {num_pedidos}: "))  # pedir ao usr um número
    sum_num += num  # update do somatório

media = sum_num / max_num  # calcula a media
print(f"media: {media}")  # mostra a media
