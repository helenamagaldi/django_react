import datetime

from carro import VeiculoLocacao
from pessoa import Pessoa
from reserva import Reserva

lista_reservas = []
lista_clientes = []

def tela_inicial():
    print("Bem vindo à locadora de carros ACME!\n")
    print("-------------------------------------\n")

    print("""
    1. Cadastro de Cliente
    2. Lista de carros disponíveis
    3. Fazer Reserva
    """)

    opcao = int(input("Por favor, digite a opção desejada dentre as disponibilizadas acima: "))

    escolha_usuario(opcao)

def escolha_usuario(opcao):
    if opcao == 1:
        print("-------------------------------------\n")
        print("-------Cadastro de Cliente-----------\n")    
        print("Olá, seja bem vinda à área de cadastro de cliente da locadora de carros ACME")
    
        cliente = Pessoa.cadastro_cliente()
        cliente.detalhes()
        lista_clientes.append(cliente)

        print("""
        Muito obrigada por fazer o seu cadastro de cliente. Seja bem vinda à ACME!
        Você está sendo redirecionada ao nosso painel de opções.
        """)

        return lista_clientes, tela_inicial()
    
    if opcao == 2:
        print("""
            Lista de carros disponíveis para locação:
            """)
        for carros in VeiculoLocacao.lista_carros:
            carros.detalhes()

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

    elif opcao == 3:
        cliente1 = Pessoa("cookie", "Cookie Monster", "kkk", "kkk")
        lista_clientes.append(cliente1)
        lista_usuarios = []

        for cliente in lista_clientes:
            lista_usuarios.insert(0, cliente.usuario)

        print(lista_usuarios)

        print("Olá, seja bem vinda à área de reservas da locadora de carros ACME")
        reserva = Reserva.fazer_reserva()
        lista_reservas.append(reserva)

        # if Reserva.usuario in lista_clientes.usuario:
        #   print ("hi")

        # if [item for item in lista_clientes["usuário"] == lista_reservas["usuário"]]:
        #   print("ok")

        user = getattr(reserva, "usuario")
        print(user) 
        print(f"lista clientes: {lista_clientes}")

        procura_cliente = filter(lambda x: x.usuario == user, lista_clientes)

        print(f"procura: {procura_cliente}")

        if procura_cliente is not None:
            print("ok")

        # if getattr(reserva, "usuario") in lista_clientes:
        #     print("ok")
        # else:
        #     print("Não há um cadastro para esse usuário. Você gostaria de cadastrá-lo?")


    # elif opcao == 3:


    # elif choice == 4:
    #     break

    else:
        print("Please enter a choice between 1-4 only!")

    # for object in lista_clientes:
    #   print(vars(object))