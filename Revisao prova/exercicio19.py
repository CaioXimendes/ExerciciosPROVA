# Usando While escreva um algoritmo que preencha um array A com os 10
# primeiros números ímpares, iniciando por zero
# saída: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor_a = []
num = 0
cont = 0
while cont < 20:
    if num % 2 != 0:
        vetor_a.append(num)
    num += 1
    cont += 1
print(vetor_a)
# n = é quando num é par
# funcionamento do while no vetor [n,1,n,3,n,5,n,7,n,9,n,11,n,13,n,15,n,17,n,19]