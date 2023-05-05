# Dado o seguinte array [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60] .
# Crie um novo array com os dados que estão entre os índices 3 e 8.

vetor_a = [10,12,20,30,25,40,32,31,35,50,60]
vetor_b = []

for x in range(3,9,1):
    vetor_b.append(vetor_a[x])
print(vetor_b)