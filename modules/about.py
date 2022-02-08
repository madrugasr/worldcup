from modules.exceptions import limpa_tela, linha, sair


def sobre():
    """
    Função: Sobre o Programa.
    """
    limpa_tela()
    print("""
    \033[34mSobre Nós!\033[m\n
    Este programa foi desenvolvido a pedido da FIFA (Federação Internacional de Futebol),
    para atender as necessidades de Gestão dos Campeonatos Mundiais da Copa do Mundo.
    
    \033[35mDesenvolvedor:\033[m Daniel Marques.\n""")

    linha(60) 

    print('\n1. Menu Inicial')
    print('\n2. Sair')
    op = input()
    #Validação das Opções
    while not (op.isnumeric()) and op != '1' and op != '2':
        print('\n\033[31mResposta Incorreta.\033[m')
        print('\n1. Menu Inicial')
        print('\n2. Sair\n')
        op = input('\n' )
    
    if op == '1': limpa_tela(), menu()
    if op == '2': limpa_tela(), sair()