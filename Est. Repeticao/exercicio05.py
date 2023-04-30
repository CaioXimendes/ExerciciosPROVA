#Altere o programa anterior permitindo ao usuário informar
# as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

pop_pais_A = int(input("Informe a população do país A: "))
while pop_pais_A != 80000:
    pop_pais_A = int(input("A população deve ser 80000, tente novamente: "))
taxa_anual_crescimento_A = float(input("Informe a taxa de crescimento do país A: "))
while taxa_anual_crescimento_A != 3:
    taxa_anual_crescimento_A = float(input("A taxa de crescimento deve ser 3%, tente novamente: "))
else:
    taxa_anual_crescimento_A = 1.03
pop_pais_B = int(input("Informe a população do país B: "))
while pop_pais_B != 200000:
    pop_pais_B = int(input("A população deve ser 200000, tente novamente:"))
taxa_anual_crescimento_B = float(input("Informe a taxa de crescimento do país B: "))
while taxa_anual_crescimento_B != 1.5:
    taxa_anual_crescimento_B = float(input("A taxa de crescimento deve ser 1.5%, tente novamente: "))
else:
    taxa_anual_crescimento_B = 1.015
cont=0
while pop_pais_A < pop_pais_B:
    pop_pais_A = pop_pais_A*taxa_anual_crescimento_A
    pop_pais_B = pop_pais_B*taxa_anual_crescimento_B
    cont+=1
print(f"{cont} anos foram necessários para o país A igualar ou ultrapassar o país B")