# Faça um programa que receba dois números inteiros e gere os números inteiros
# que estão no intervalo compreendido por eles.

x = int(input("Informe o primeiro número do intervalo: "))
y = int(input("Informe o segundo número do intervalo: "))
if x > y:
    z= -1
else:
    z= 1
for n in range (x,y,z):
    print(n)