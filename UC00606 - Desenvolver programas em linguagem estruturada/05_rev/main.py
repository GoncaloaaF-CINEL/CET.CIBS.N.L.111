
lst  = [1,3,5,6,7,10]

lst.sort() # ordenar a lista

print(lst)


lst  = [1,3,5,6,7,10]

lst.sort(reverse=True)

print(lst)

print(lst.__len__()) # num de elm na lista # conta os elm na lista
print(len(lst))      # num de elm na lista


nomes = ["Carlos", "Ana", "João", "Beatriz", "Miguel", "Sofia", "Rui", "Inês"]

nomes.sort()
print(nomes)

print(len(nomes))
print(nomes.__len__())


print("-----------")
lst2  = [[1,3,5,5],
        [1,4],
        [1,3,5,6]]

print(len(lst2))
print(len(lst2[0]))
print(len(lst2[1]))
print(len(lst2[2]))

print("-----------")

nomes = [
    "Tiago", "Ana", "Bruno", "Sofia", "Rui", "Carla", "Miguel", "Inês","Pedro", "Joana",
    "Filipe", "Marta", "Ricardo", "Beatriz", "Daniel", "Catarina", "Luís", "Patrícia", "André", "Mariana",
    "Nuno", "Cláudia", "Gonçalo", "Teresa", "Vítor", "Andreia", "Paulo", "Helena", "Diogo", "Liliana",
    "Hugo", "Rita", "Fábio", "Susana", "Marco", "Diana", "Alexandre", "Vanessa", "Sérgio", "Filipa",
    "Jorge", "Raquel", "Eduardo", "Sónia", "Joel", "Célia", "Tomás", "Elisabete", "Ivo", "Mónica"
]

print("-----------")
print(nomes.index("Diana")) # idx de um nome

print("-----------")





print(len(nomes))

print(nomes[-1]) # last elm
print(nomes[49])

print("-----------")
print(nomes[0])
print(nomes[len(nomes)-1]) # <=> nomes[-1]
print("-----------")
print(nomes[-49])
print(nomes[-50])

print("-----------")

print("Fernando")

print("---------")


print(nomes[3:9]) # [n:m] - n ate m-1

print(nomes[:9]) # [:m] - 0 ate m-1

print(nomes[40:]) # [n:] - n ate ao ultimo elm


print("---------")


print(nomes[10:31:5])


print("---------")
print(nomes[::-10]) # 50, 39, 29, 19, 9

print(nomes.index("Liliana"))

print("---------")


print(nomes[::10]) # 0, 10, 20, 30, 40, 50

print(nomes.index("Tiago"))
print(nomes.index("Mónica"))
"""
se idx pos -> 
se idx neg <-

"""

print("---------")


nomes = [
    "Tiago", "Ana", "Bruno", "Sofia", "Rui", "Carla", "Miguel", "Inês","Pedro", "Joana"
]

print(nomes[-1])
print(nomes[-5])

print(nomes[-5:-1])
print(nomes[-5:])

print("---------")
print("---------")

# ['Carla', 'Miguel', 'Inês', 'Pedro', 'Joana']
resp = nomes[-5:]
resp.reverse()
print(resp)

print("---------")

print(nomes[-5:][::-1])
print("---------")
print(nomes[:-6:-1])

print("---------")


## imagine que tem a lista

nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

# como obter
# ['Bruno', 'Carlos']



# os ultimos 2 elm

# a lista invetida

# os nomes nas pos par (0 é par)


"""
tendo a lista: 
numeros = [10, 20, 30, 40, 50, 60, 70, 80]

Mostrar os 3 primeiros números
Mostrar os 3 últimos números
Mostrar os números do índice 2 ao 6
Mostrar a lista invertida
Mostrar os números de 2 em 2
Mostrar os últimos 4 números invertidos

todos os valores pares 
a soma de todos os impares 
soma os ultimos 2 
soma os 1os 2

soma os 3 e 4 com os 2 ultimos

"""



## list slicing com strings

nome = "Gonçalo" # -> ['G', 'o', 'n', 'c', 'a', 'l', 'o']

print(nome[0])
