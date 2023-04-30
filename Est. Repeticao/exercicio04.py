#Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes
# com uma taxa de crescimento de 1.5%

#Faça um programa que calcule e escreva o número de anos necessários
# para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

pop_pais_A = 80000
taxa_anual_crescimento_A = 1.03
pop_pais_B = 200000
taxa_anual_crescimento_B = 1.015
cont=0

while pop_pais_A < pop_pais_B:
    pop_pais_A = pop_pais_A*taxa_anual_crescimento_A
    pop_pais_B = pop_pais_B*taxa_anual_crescimento_B
    cont+=1
print(f"{cont} anos foram necessários para o país A igualar ou ultrapassar o país B")