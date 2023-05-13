# Exercícios envolvendo Tuplas

#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ("banana",2.5,"feijao",4,"arroz",3.5,"macarrao",1.5)
cont = 0
for x in tupla:
    if type(x) == str:
        print(f"Produto: {x}", end= "   ")
    else:
        print(f"Preço: R${x}")