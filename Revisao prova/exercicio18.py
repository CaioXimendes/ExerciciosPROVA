# Escreva um algoritmo que dado um arrays, retorno um novo array, com os elementos em ordem invertida.
# entrada: a=[2,5,4,2,8,5,2]
# saída: b=[2,5,8,2,4,5,2]

vetor_a = [2,5,4,2,8,5,2]
vetor_b = []

for i in range (6,-1,-1):
    vetor_b.append(vetor_a[i])
print(vetor_b)