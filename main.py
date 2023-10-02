import classes as c

if __name__ == "__main__":
    opcao = None
    arvore = c.ArvoreBinariaBusca()

    while opcao != 0:
        print("-------------------------------------")
        print("Escolha uma opção:")
        print("1 - Inserir elemento;")
        print("2 - Remover elemnto;")
        print("3 - Pesquisar elemento;")
        print("4 - Imprimir árvore completa;")
        print("0 - Encerrar sistema.")
        opcao = int(input())

        match opcao:
            case 1:

                #INSERIR ELEMENTO
                print("-------------------------------------")
                print("Informe o elemento à ser inserido: ")
                valor = int(input())
                arvore.inserir(valor)
                print("-------------------------------------")
                print("Valor", valor, "inserido!")
            case 2:

                #REMOVER ELEMENTO
                print("-------------------------------------")
                print("Informe o elemento à ser removido: ")
                valor = int(input())
                arvore.remover(valor)
                print("-------------------------------------")
                print("Valor", valor, "removido!")
            case 3:

                #PESQUISAR ELEMENTO
                print("-------------------------------------")
                print("Informe o elemento à ser pesquisado: ")
                valor = int(input())
                retorno = arvore.pesquisar(valor)
                if retorno is None:
                    print("-------------------------------------")
                    print("Valor", valor, "não encontrado!")
                else:
                    print("-------------------------------------")
                    print("Valor", retorno.raiz.data, "encontrado!")
            case 4:

                #IMPRIMIR A ÁRVORE
                print("-------------------------------------")
                arvore.imprimir(1)
            case 0:

                #FECHAR PROGRAMA
                print("Encerrando programa...")
                exit()