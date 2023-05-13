# Exercício Python 72:
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze",
         "quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

pergunta = int(input("Informe um número: "))

for x, extenso in enumerate(tupla):
    if pergunta == x:
        extenso = tupla[x]
        print(f"O número {pergunta}, por extenso é: {extenso}")