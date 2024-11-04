import os


def adicionar(contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    os.system("clear")
    print(f"Contato adicionado {nome} com sucesso!")
    return


def ver_contatos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        status = " ❤ " if contato["favorito"] else " "
        nome = contato["nome"]
        email = contato["email"]
        telefone = contato["telefone"]
        print(f"{indice}. Nome: {nome} {status}")
        print(f"Telefone: {telefone}")
        print(f"Email: {email}")
    return


def editar_contato(contatos, indice_contato, novo_telefone):
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado]["telefone"] = novo_telefone
        print(f"Contato {indice_contato} atualizado para {novo_telefone}")
    else:
        print("Índice inválido")

    return


def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if contatos[indice_contato_ajustado]["favorito"] == True:
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {indice_contato} desfavoritado com sucesso")
    else:
        contatos[indice_contato_ajustado]["favorito"] == ""
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} favoritado com sucesso")

    return


def ver_contatos_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"] == True:
            status = " ❤ " if contato["favorito"] else " "
            print(f"{indice}. Nome: {contato['nome']} {status}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")

    return


def apagar_contato(contatos, indice_contato):
    print(indice_contato)
    removido = contatos.pop(int(indice_contato) - 1)
    print(f'Contato {removido["nome"]} excluído com sucesso!')
    return


contatos = []
while True:
    print("\n1. Adicionar novo contato")
    print("2. Visualizar a lista de contatos cadastrados.")
    print("3. Editar um contato.")
    print("4. Marcar/desmarcar um contato como favorito")
    print("5. Ver a lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")
    escolha = input("\nDigite a opção desejada: ")
    os.system("clear")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o Email: ")
        adicionar(contatos, nome, telefone, email)

    if escolha == "2":
        ver_contatos(contatos)

    if escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Qual contato deseja alterar: ")
        novo_telefone = input("Digite o novo número de telefone: ")
        editar_contato(contatos, indice_contato, novo_telefone)

    if escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Qual contato deseja favoritar?: ")
        favoritar_contato(contatos, indice_contato)

    if escolha == "5":
        ver_contatos_favoritos(contatos)

    if escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Qual contato deseja apagar?: ")
        apagar_contato(contatos, indice_contato)

    if escolha == "7":
        break
