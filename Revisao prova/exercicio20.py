# Escreva um algoritmo que receba do usuário 10 números e mostre:
# 1. todos os números ímpares;
# 2. todos os números pares;
# 3. todos os números positivos;
# 4. todos os números negativos;
# 5. todos os zeros que aparecem no array

vetor_a = []

for x in range (10):
    vetor_a.append(float(input("Digite um número: ")))

for i in range (10):
    if vetor_a[i] != 0:
        if vetor_a[i] % 2 != 0:
            if vetor_a[i] > 0:
                print(f"num impar positivo na posição {i}: {vetor_a[i]}")
            else:
                print(f"num impar negativo na posição {i}: {vetor_a[i]}")
        else:
            if vetor_a[i] > 0:
                print(f"num par positivo na posição {i}: {vetor_a[i]}")
            else:
                print(f"num par negativo na posição {i}: {vetor_a[i]}")
    else:
        print(f"num igual a zero na posição {i}: {vetor_a[i]}")