# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Flamengo.

tupla = ("Botafogo", "Palmeiras", "Fluminense", "Athletico-PR", "Cruzeiro", "Fortaleza", "São Paulo", "Flamengo",
         "Atlético-MG", "Santos", "Grêmio", "Bahia", "Internacional", "Vasco", "Bragantino", "Corinthians",
         "Cuiabá", "Goiás", "Coritiba", "América-MG")
cont = 0

for x, times in enumerate(tupla):
    if x < 5:
        print(f"Time nº {x+1} é o {times}")
    if x > 15:
        print(f"Ultimos colocados são os times: {times}, na posição: nº {x+1}")
    if times == "Flamengo":
        cont = x
print()
print("times em ordem alfabética: \n")\

for times2 in sorted(tupla):
    print(f"time: {times2}")

print(f"O flamengo está na posição {cont+1}")
