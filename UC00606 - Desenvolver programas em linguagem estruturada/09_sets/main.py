myset = {"item", "item2", "item3", "item3"}

print(myset)

print(type(myset))

print(len(myset)) ## <--


print("item" in myset)
print("item33" in myset)

print("--")
print("item" not in myset)
print("item33" not in myset)
print("--")

for item in myset:
    print(item)


print("--")

myset.add("item4")
print(myset)


print("--")
myset3 = {"item", "item2", "item3"}
myset4 = {"item4", "item5", "item6"}
myset5 = {"item3", "item1", "99999999999"}

print(myset3)

myset3.add("rato") # add 1 elm

print(myset3)

myset3.update(myset5)

print(myset3)


print("--")
myset6 = {"item", "item2", "item3"}


myset6.update(myset4, myset5)
print(myset6)


myset6.remove("99999999999")
print(myset6)

#myset6.remove("99999999999")

myset6.discard("item1")
print(myset6)


print("----")

myset6.pop()
print(myset6)



print("----")
myset6.clear() # <- limpa os dados
print(myset6)

print("----")

del myset6  # <- limpa da  memoria

pao_de_queijo = {
    "polvilho doce",
    "leite",
    "óleo",
    "ovos",
    "queijo ralado",
    "sal"
}

bolo_de_polvilho = {
    "ovos",
    "polvilho doce",
    "açúcar",
    "óleo",
    "leite",
    "fermento em pó",
    "pitada de sal"
}


print(pao_de_queijo.union(bolo_de_polvilho))
print(pao_de_queijo.intersection(bolo_de_polvilho))
print(pao_de_queijo.difference(bolo_de_polvilho))
print(bolo_de_polvilho.difference(pao_de_queijo))

print(pao_de_queijo.symmetric_difference(bolo_de_polvilho))


print("----")
print(pao_de_queijo & bolo_de_polvilho) # intersection
print(pao_de_queijo ^ bolo_de_polvilho) # symmetric_difference
print(pao_de_queijo | bolo_de_polvilho) # union
print(pao_de_queijo - bolo_de_polvilho) # difference


print("----")
print(pao_de_queijo)
pao_de_queijo.symmetric_difference_update(bolo_de_polvilho)
print(pao_de_queijo)