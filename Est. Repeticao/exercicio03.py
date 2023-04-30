# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Informe o seu nome: ")
while len(nome) <= 3:
    nome = input("Seu nome precisa ter mais de 3 caracteres, tente novamente: ")
idade = int(input("Informe a sua idade: "))
while idade <0 or idade >150:
    idade = int(input("Sua idade deve estar entre 0 e 150, tente novamente: "))
salario = float(input("Informe o seu salário: "))
while salario <=0:
    salario = float(input("Salário deve ser maior que zero, tente novamente:"))
sexo = input("Informe o seu sexo: 'f' ou 'm': ")
while sexo != "f" and sexo != "m":
    sexo = input("Seu sexo não pode ser diferente de: 'f' ou 'm', tente novamente: ")
estado_civil = input("Informe o seu estado civil: 's', 'c', 'v', 'd': ")
while estado_civil != "s" and estado_civil != "c"and estado_civil != "v" and estado_civil != "d":
    estado_civil = input("Seu estado civil não pode ser diferente de: 's', 'c', 'v', 'd', tente novamente: ")