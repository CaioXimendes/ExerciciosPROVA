# Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo de Xadrez
# (considere apenas horas inteiras, sem os minutos)
# e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas
# e que o jogo pode iniciar em um dia e terminar no dia seguinte

hora_inicio = int(input("Informe a hora de inicio do jogo de xadrez, apenas números inteiros e sem minutos: "))
hora_fim = int(input("Informe a hora de término do jogo de xadrez, apenas números inteiros e sem minutos: "))
pergunta = "f"
if hora_inicio == hora_fim:
    while pergunta != "s" and pergunta != "n":
        pergunta = input("O jogo foi até o dia seguinte? s/n: ")
        if pergunta == "s":
            print("A duração do jogo foi de 24 horas")
        elif pergunta =="n":
            print("A duração do jogo foi de até 59 minutos")
        else:
            print("Não reconheci sua resposta, tente novamente!")
elif hora_inicio > hora_fim:
    duracao_jogo = (hora_fim-hora_inicio)+24
    print(f"A duração do jogo foi: {duracao_jogo} horas")
else:
    duracao_jogo = (hora_fim-hora_inicio)
    print(f"A duração do jogo foi: {duracao_jogo} horas")