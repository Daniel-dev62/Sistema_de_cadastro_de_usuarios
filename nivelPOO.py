#CADASTRO DE USUÁRIO COM JSON
#1 - Cadastrar usuário
#2 - Listar usuários
#3 - Buscar usuário
#4 - Sair

import json
import time

try:
    with open("usuarios.json","r") as f:
        usuarios= json.load(f)
except FileNotFoundError:
    usuarios= []


#salvando os dados em json
def salvar():
    with open("usuarios.json","w") as f:
        json.dump(usuarios, f, indent=4)

#cadastrando os dados em json
def cadastro_usuario():         
    p1= input("Digite seu nome de cadastro: ").capitalize().strip()

    for usuario in usuarios:
        if usuario["Nome"] == p1:
            print("Usuário já cadastrado! ")
            return
        
    usuarios.append({
         "Nome":p1
         }) 
        
    print("Nome cadastrado! ")     
    salvar()

#listando dados em json
def listar_usuario():
    if not usuarios:
        print("Nenhum usuario cadastrado!")
    else:
        for x in usuarios:
            print(x)

#buscando dados em json
def buscar_usuario():
    p1= input("Digite o nome da usuario desejado: ").capitalize() .strip()

    for usuario in usuarios:
        if usuario ['Nome']== p1:
            print(f"O cara foi encontrado: {usuario['Nome']}")
            return
    else:
        print("Usuário não cadastrado!")


#Inicio
while True:
    p1= int(input(" 1- Cadastrar Usuário\n 2- Listar Usuário\n 3- Buscar Usuário\n 4- Sair\n Digite a opção desejada: "))
    time.sleep(3)
    if p1 == 1:
        cadastro_usuario()
        time.sleep(1)
    elif p1 == 2:
        listar_usuario()
        time.sleep(1)
    elif p1 == 3:
        buscar_usuario()
        time.sleep(1)
    elif p1 == 4:
        print("Você saiu do painel! ")
        break
    