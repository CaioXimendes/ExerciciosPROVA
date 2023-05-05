# Escreva um algoritmo para ler dois valores (considere que não serão lidos
# valores iguais) e escrevê-los em ordem crescente

# est. repeticao caso não queira ler num igual
#while num_2 == num_1:
#    num_1 = float(input("Digite um número: "))
#    num_2 = float(input("Digite outro número: "))
#    if num_2 == num_1:
#        num_2 = float(input("O número 2 não pode ser igual ao número 1, tente novamente: "))

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite outro número: "))

if num_1 > num_2:
    print(f"{num_2}, {num_1}")
else:
    print(f"{num_1}, {num_2}")