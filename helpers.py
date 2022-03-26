from script import tela_inicial

def opcao_voltar():

    voltar = input("Gostaria de voltar para a nossa tela principal? Digite 'S' para sim e 'N' para não")

    if voltar == "S":
        tela_inicial()
    elif voltar == "N":
        print("""
        A ACME locadora de veículos deseja uma vida longa e próspera
        """)
    else:
        print("""
        Opção inválida, termination process begin
        """)