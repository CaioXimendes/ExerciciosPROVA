#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário
#mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario = input("Informe seu nome de usuário: ")
senha_usuario = input("Informe sua senha: ")
while senha_usuario == nome_usuario:
    senha_usuario = input("Senha não pode ser igual ao nome de usuário, tente novamente: ")
else:
    print("Login realizado com sucesso!")