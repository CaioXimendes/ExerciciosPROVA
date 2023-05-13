#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla.

# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input("Informe um número:")),
         int(input("Informe um número:")),
         int(input("Informe um número:")),
         int(input("Informe um número:")))

print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O valor 3 apareceu na posição {tupla.index(3)+1}")
else:
    print("Não foi detectado o valor 3 na tupla!")
print("Valores pares digitados foram: ",end="")
for x in tupla:
    if x % 2 == 0:
        print(x, end= " ")