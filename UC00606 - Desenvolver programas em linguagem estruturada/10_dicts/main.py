carro ={
    "marca":"BMW",
    "modelo":"320d",
    "cor":"Amarelo"
}

print(carro)

print(carro["marca"])
print(carro["modelo"])


print(carro.get("COR", "Campo invalido"))


print(carro.keys())
print(carro.values())
print(carro.items())


carro["modelo"] = "X7"
print(carro)

carro.update({"modelo":"X9"})
print(carro)


print("------")

carro["CC"] = 3000

print(carro)

carro.update({"matricula":"00AA00"})

print(carro)

print(carro.__len__())
print(len(carro))

print(carro)

print(carro.pop("cor"))
print(carro)

print(carro.popitem()[0])
print(carro.popitem()[1])

print(carro)

del carro["modelo"]

print(carro)

carro.clear()

print(carro)

carro ={
    "marca":"BMW",
    "modelo":"320d",
    "cor":"Amarelo"
}

for k, v in carro.items():
    print(k, v)


for k in carro.keys():
    print(k)

for k in carro.values():
    print(k)


print("-------")

for k in carro:
    print(k)




print("-------" * 6)
empresa = {
    "TI": {
        "infraestrutura": {
            "responsavel": "Alice",
            "servidores": 5
        },
        "desenvolvimento": {
            "linguagem": "Python",
            "equipa": ["Bob", "Carlos", "Alice", "Fernando", "Marina"]
        }
    },
    "RH": {
        "recrutamento": {
            "vagas_abertas": 3
        }
    }
}

print(empresa["TI"]["desenvolvimento"]["equipa"][0])

dev = empresa["TI"]["desenvolvimento"]

print(dev)

print(empresa.get("Vendas", "dpt invalido"))

empresa["Vendas"] = {}

print(empresa.get("Vendas", "dpt invalido"))