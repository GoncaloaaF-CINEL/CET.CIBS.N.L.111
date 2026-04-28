"""

[] -> List
() -> Tuplo


"""

nomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]


print(nomes)
print(nomes[0])

print(nomes.__len__())
print(len(nomes))

nomes[0] = "Rita"
print(nomes[0])


print(nomes)
nomes.append("Rafael")
print(nomes)

for elm in nomes:
    print(elm)

print("--" * 10)

for i, elm in enumerate(nomes):
    print(i, elm)




print("----" * 10)
print("Tuplos")
print("----" * 10)

aluno = ("Carlos", 18)

print(aluno)
print(aluno[0])
print(aluno[1])

# print(aluno[4])


# aluno[1] = 12 <- não podem mudar valores
aux = list(aluno)
aux[1] = 12 # é uma lista
aluno = tuple(aux)

print(aluno)

tp1 = (18, 18)
print(tp1)

print("------")

nome = aluno[0]
nota = aluno[1]
print(nome)
print(nota)

print("------")

nome1, nota1 = aluno
print(nome1)
print(nota1)


for i, elm in enumerate(nomes):
    print(type(elm))



tp2 = (112,21,31,13,51,21,31,13,41,4124,234,34,21412,12)
for num in tp2:
    print(num)



UCs   = ["uc1", "uc2", "uc3", "uc4"]
notas = [15,12,12,19]

notas2 = [("uc1", 15.0),("uc2", 12.4),("uc3", 12),("uc4", 19), ]