# importando a variável os - usada para interagir com o sistema operacional
import os

# lista que armazena mensagens
mensagens = []

# recebe o nome do usuário que quer entrar no chat
nome = input("Nome: ")

# começando um loop infinito
while True:
    # limpando terminal (cls = windows)
    os.system('cls')

    # verificando se tem mensagens gravadas na lista
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("__________________________________")

    # obtendo texto
    texto = input("Mensagem: ")
    if texto == "fim":
        break

    # adicionando mensagens na lista, que contém dicionários
    mensagens.append({
        "nome": nome,
        "texto": texto
    })