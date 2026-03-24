lst = [1, 2, 3]
lista_nomes = ["Ana", "Maria", "Joana", "Rita"]

print(lst)
print(lista_nomes)

lst.append(99)  # add no final

print(lst)

lista_nomes.append("Luis")
print(lista_nomes)

# lst[idx]
print(lst[2])

lst = [1, 2, 3, 6, 7, 1, 9, 12, 5]

print(lst[1])
lst[1] = 912
print(lst[1])

print(lst)

lst.append(888)
print(lst)

lst.insert(2, 456)  # add no index indicado

print(lst)

# Criamos
# ler tudo
# let idx

# mudar valor

# add no fim
# add no inicio/meio


print(lst.__len__())
print(len(lst))

################
print("-----------")
print("-----------")
lst2 = [5, 6, 1, 4]
print(lst2)
print(len(lst2))  # len -> num de elm na lista ->4

lst2.append(99)
print(len(lst2))
print("--")
print(lst2[2])

# Faça um Programa com uma lista com 5 números inteiros e mostre-os.

lista_num = [1, 2, 3, 4, 5]

print(lista_num)

# Faça um Programa que peça 5 números ao utilizador. -> done
# Adicione esses números a uma lista -> done
# mostre o conteúdo da lista

lista2 = []

for i in range(1, 6):
    num = int(input(f"Digite o {i}º número: "))
    lista2.append(num)

print(lista2)
