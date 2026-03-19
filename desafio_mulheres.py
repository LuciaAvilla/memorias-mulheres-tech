mulheres_tech = []
opcao = 0
arquivo = "memorias_mulheres_tech.txt"


def filtro_texto(mensagem):

    while True:

        dados = input(mensagem).strip()

        if dados == "":
            print("Erro: Este campo não pode ficar vazio.")
        else:
            return dados


def filtro_ano(mensagem):

    while True:
        try:
            ano = int(input(mensagem))
            return ano
        except ValueError:
            print("Erro: Digite o ano apenas com números.")


while opcao != "5":

    print("\n" + "="*50)
    print("Mulheres que fizeram diferença na área Tech.\nCadastre ou saiba mais sobre elas!")
    print("1 - Cadastrar Mulher Tech")
    print("2 - Listar Histórico")
    print("3 - Buscar por nome")
    print("4 - Exibir Estatística")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    print("\n" + "="*50)

    if opcao == "1":

        nome = filtro_texto("Nome: ")
        area_atuacao = filtro_texto("Área de Atuação: ")
        contribuicao = filtro_texto("Contribuição ou feito relevante: ")
        periodo = filtro_ano("Ano ou periodo: ")

        ficha_mulher = {
            "nome": nome,
            "area_atuacao": area_atuacao,
            "contribuicao": contribuicao,
            "periodo": periodo,
        }

        mulheres_tech.append(ficha_mulher)

        with open("memorias_mulheres_tech.txt", "a", encoding="utf-8") as file:
            linha = f"Nome: {nome} | Área: {area_atuacao} | Contribuição: {contribuicao} | Ano: {periodo}\n"
            file.write(linha)

        print("Mulher de Tech cadastrada com sucesso!")

    elif opcao == "2":

        try:
            with open("memorias_mulheres_tech.txt", "r", encoding="utf-8") as arquivo:
                print("\n--- HISTÓRICO DE MULHERES NA TECH ---")

                for linha in arquivo:
                    print(linha.strip())

        except FileNotFoundError:
            print("Ainda não existem registros no histórico")

    elif opcao == "3":

        buscar_mulher = filtro_texto(
            "Digite a Mulher em Tech que deseja buscar: ")

        encontrada = False

        for ficha_mulher in mulheres_tech:

            if buscar_mulher.lower() in ficha_mulher["nome"].lower():
                print("\n--- Mulher Encontrada ---")
                print(f"Nome: {ficha_mulher['nome']}")
                print(f"Área: {ficha_mulher['area_atuacao']}")
                print(f"Contribuição: {ficha_mulher['contribuicao']}")
                print(f"Ano: {ficha_mulher['periodo']}")

                encontrada = True

        if not encontrada:
            print(
                f"Nenhuma Mulher em Tech com o nome '{buscar_mulher}' foi encontrada.")

    elif opcao == "4":

        if not mulheres_tech:
            print("\nAinda não existem dados cadastrados para gerar estatísticas.")
        else:
            total = len(mulheres_tech)

            anos = []

            for mulher in mulheres_tech:
                anos.append(mulher['periodo'])

            ano_mais_antigo = min(anos)
            ano_mais_recente = max(anos)

            print("\n--- ESTATÍSTICAS DO SISTEMA ---")
            print(f"Total de mulheres cadastradas: {total}")
            print(f"Pioneira mais antiga registrada: {ano_mais_antigo}")
            print(f"Pioneira mais recente registrada: {ano_mais_recente}")
            print("\n" + "="*50)

    elif opcao == "5":
        print("\n" + "="*50)
        print("ENCERRANDO O SISTEMA DE MEMÓRIAS ")
        print(" Este arquivo existe porque histórias importam.")
        print("Mulheres sempre estiveram presentes na tecnologia.")
        print("E agora,você faz parte dessa transformação.")
        print("="*50 + "\n")
