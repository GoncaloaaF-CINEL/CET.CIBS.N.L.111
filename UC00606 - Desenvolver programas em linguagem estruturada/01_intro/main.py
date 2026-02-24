nome = "Gonçalo"  # criar uma var

print(nome)  # escreve na consola

"""

Tipdos de dados 

int  -
string - 
float - 
bool -

"""

idade = 12
nome = "Gonçalo"
altura = 1.2
aprovado = True

#      :typeHint
idade2: int = 12
nome2: str = "Gonçalo"
altura2: float = 1.2
aprovado2: bool = True

print("---------")

print(idade2)
idade2 = "Dez"

print(idade2)

print("-----------------")

# cmt 1 linha

"""

cmt 
multi
linha

"""

"""

idade = 231
idade2 = "999" -> txt -> " "

idade_txt = str(idade)
idade2_int = int(idade2) -> converte idade2 para int


\n - Quebra de linha, passa para linha de baixo
\t - tab
"""
idade2 = 21
print(nome2, idade2, altura2, aprovado2)

print("nome: " + nome2 +
      "\nidade: " + str(idade2) +
      "\naltura: " + str(altura2) +
      "\naprovado: " + str(aprovado2))

print(f"Nome:\t\t{nome2}\nIdade:\t\t{idade2}\nAltura:\t\t{altura2}\nAprovado:\t{aprovado2}")

print("------------")

# input


nome = input("Digite seu nome: ")
idade = input("Digite a sua idade: ")
print(f"ola {nome}, tens {idade} anos")

print("------------")

print(type(idade))

idade_i = int(idade)  # transformar a idade em str para idade em int

print(type(idade_i))

ano_nasc = 2026 - idade_i

print(f"ola {nome}, tens {idade} anos e nascste em {ano_nasc}")
# op com var


"""
1 Faça um Programa que mostre a mensagem "ola mundo" na consola.
2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. 
--

3 Faça um Programa que peça dois números e imprima a soma.
4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
--




"""
