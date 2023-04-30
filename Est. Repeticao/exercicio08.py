# Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for x in range(5):
    num = float(input(f"Informe o número {x}: "))
    soma = soma + num
media = soma/5
print(f"A soma entre os 5 números foi: {soma} e a média foi: {media}")