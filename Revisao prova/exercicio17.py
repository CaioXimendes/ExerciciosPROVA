# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
# compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
# calcule e escreva o custo total da compra.

macas_compradas = int(input("Informe a quantidade de maçãs compradas: "))
custo_maior = 1.3
custo_menor = 1

if macas_compradas >= 12:
    custo_final = macas_compradas*custo_menor
    print(f"O custo total da compra foi: R$ {custo_final}")
else:
    custo_final = macas_compradas*custo_maior
    print(f"O custo total da compra foi: R$ {custo_final}")
    print("Eita maçã cara da peste 😂")