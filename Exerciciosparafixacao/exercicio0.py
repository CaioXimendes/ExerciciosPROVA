#Exercicios envolvendo tuplas

# Exercício Python 077 Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ("arroz","feijao","macarrao","banana")

for x in lista:
    for y in x:
        if y in "aeiouAEIOU":
            print(y, end= "  ")