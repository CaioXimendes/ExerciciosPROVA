# Faça um programa que leia 5 números e informe o maior número.

num_2 = 0

for x in range (1,6):
    num = float(input(f"Informe o número {x}:"))
    if num > num_2:
        num_2 = num
print(f"O maior número foi {num_2}")