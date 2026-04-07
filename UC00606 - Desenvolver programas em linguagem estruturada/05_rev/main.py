
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
    "Tiago", "Ana", "Bruno", "Sofia", "Rui", "Carla", "Miguel", "Inês",
    "Pedro", "Joana", "Filipe", "Marta", "Ricardo", "Beatriz", "Daniel", "Catarina",
    "Luís", "Patrícia", "André", "Mariana", "Nuno", "Cláudia", "Gonçalo", "Teresa",
    "Vítor", "Andreia", "Paulo", "Helena", "Diogo", "Liliana", "Hugo", "Rita",
    "Fábio", "Susana", "Marco", "Diana", "Alexandre", "Vanessa", "Sérgio", "Filipa",
    "Jorge", "Raquel", "Eduardo", "Sónia", "Joel", "Célia", "Tomás", "Elisabete",
    "Ivo", "Mónica"
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

