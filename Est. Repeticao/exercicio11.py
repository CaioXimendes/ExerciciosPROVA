# Altere o programa anterior para mostrar no final a soma dos números.
soma = 0
x = int(input("Informe o primeiro número do intervalo: "))
y = int(input("Informe o segundo número do intervalo: "))
if x > y:
    z= -1
else:
    z= 1
for n in range (x,y,z):
    print(n)
for i in range(x,y,z):
    soma = soma + i
print(f"A soma entre os números do intervalo informado é: {soma}")