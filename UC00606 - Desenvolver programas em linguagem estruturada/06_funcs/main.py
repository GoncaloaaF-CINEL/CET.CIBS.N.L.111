# saudacao("Gonçalo")
from traitlets import Int


# func para mostrar a msg
def ola_mundo():
    """
    func para mostrar a msg

    :return:
    """
    saudacao("Gonçalo")
    print("-----------------")
    print("--- ola mundo ---")
    print("-----------------")
    print(" ")



#              TYPE HINT
def saudacao(nome:str):
    print(
f"""--------------------------
--- bem vindo {nome} ----
--------------------------
"""
    )
    print(" ")


saudacao("Gonçalo")
saudacao("Maria")
saudacao("Joao")


print("--" * 10)

def soma(val1:int, val2:int):
    # res = val1 + val2
    # print("fn",res)
    return val1 + val2

# soma(10, 20)

# (a + b) * (b + c)

a = 10
b = 20
c = 30

v1 = soma(a, b)
print("fora", v1)

v2 = soma(b, c)
print("fora", v2)

calc1 = v1 * v2
print("res1 ", calc1)

calc2 = soma(a, b) * soma(b, c)
print("res2 ", calc2)



"""
1 Crie uma função msg  que mostre a msg ola mundo 
2 Crie uma função saudação  que mostre a msg ola [nome], bem vindo 
3 crie uma função que permita cirar uma var com a msg ola [nome], bem vindo
    mostre o a msg (fora da função)



"""