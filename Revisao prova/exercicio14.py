# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
# calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
# C = ((F - 32)/9)*5
# Observação: Para testar se a sua resposta está correta saiba que 100 ⍛C = 212 F

temp_f = float(input("Informe a temperatura em graus Fahrenheit: "))
temp_c = ((temp_f - 32)/9)*5
print(f"A conversão de {temp_f} graus Fahrenheint em graus celsius é: {temp_c}ºC")