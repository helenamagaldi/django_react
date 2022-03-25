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
        Você está sendo redirecionada para o nosso painel de opções.
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

        print("Olá, seja bem vinda à área de reservas da locadora de carros ACME")

        reserva = Reserva.requisitar_reserva()
        lista_reservas.append(reserva)
        user = getattr(reserva, "usuario")

        for usuario_existente in lista_clientes:
            if usuario_existente.usuario == user:
                carro_escolhido = int(input("Por favor, digite o código do carro escolhido"))
                for carro_existente in VeiculoLocacao.lista_carros:
                    if carro_existente.codigo_do_carro == carro_escolhido:
                        carro_escolhido = carro_existente
                        Reserva.montar_reserva(reserva.codigo_da_reserva,usuario_existente.usuario,carro_escolhido) 
                        print(VeiculoLocacao.lista_carros)
                        VeiculoLocacao.lista_carros.remove(carro_existente)
                        print(VeiculoLocacao.lista_carros)

            else:
                print("notok")

    else:
        print("Please enter a choice between 1-4 only!")
