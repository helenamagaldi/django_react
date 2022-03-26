import datetime
from tracemalloc import stop

from carro import Carro, VeiculoLocacao
from cliente import Cliente
from reserva import Reserva


def tela_inicial():
    print("Bem vindo à locadora de carros ACME!\n")
    print("-------------------------------------\n")

    print("""
    1. Cadastro de Cliente
    2. Lista de carros disponíveis
    3. Fazer Reserva
    4. Detalhes de Reserva
    5. Cadastro de Veículo de Locação
    """)

    opcao = int(input("Por favor, digite a opção desejada dentre as disponibilizadas acima: "))

    escolha_usuario(opcao)

def opcao_voltar():

    voltar = input("Gostaria de voltar para a nossa tela principal? Digite 'S' para sim e 'N' para não: ")

    if voltar == "S" or "s":
        tela_inicial()
    elif voltar == "N" or "n":
        print("""
        A ACME RentACar deseja uma vida longa e próspera
        """)
    else:
        print("""
        Opção inválida, termination process begin
        """)

def escolha_usuario(opcao):
    if opcao == 1:
        print("-------------------------------------\n")
        print("-------Cadastro de Cliente-----------\n")    
        print("Olá, seja bem vinda à área de cadastro de cliente da ACME RentACar")
    
        cliente = Cliente.cadastro_cliente()
        cliente.detalhes()
        Cliente.lista_clientes.append(cliente)

        print("""
        Muito obrigada por fazer o seu cadastro de cliente. Seja bem vinda à ACM RentACar!
        Você está sendo redirecionada para o nosso painel de opções.
        """)

        return Cliente.lista_clientes, tela_inicial()
    
    if opcao == 2:
        print("""
            Lista de carros disponíveis para locação:
            """)
        for carros in VeiculoLocacao.lista_carros:
            carros.detalhes()

        opcao_voltar()

    elif opcao == 3:
        lista_usuarios = []

        for cliente in Cliente.lista_clientes:
            lista_usuarios.insert(0, cliente.usuario)

        print("""
        Olá, seja bem vinda à área de reservas da ACME RentACar
        """)

        if VeiculoLocacao.lista_carros == []:
            print("Sentimos muito, mas não há mais veículos disponíveis para locação")
        else:              
            reserva = Reserva.requisitar_reserva()
            Reserva.lista_reservas.append(reserva)
            user = getattr(reserva, "usuario")

            usuario_existente = next(cliente for cliente in Cliente.lista_clientes if cliente.usuario == user)

            if usuario_existente.usuario == user:
                carro_escolhido = int(input("Por favor, digite o código do carro escolhido: "))
                carro_existente = next(carro for carro in VeiculoLocacao.lista_carros if carro.codigo_do_carro == carro_escolhido)

                if carro_existente is not None:
                    nova_reserva = Reserva.montar_reserva(reserva.codigo_da_reserva,usuario_existente.usuario,carro_existente)
                    Reserva.lista_reservas.append(nova_reserva)
                    VeiculoLocacao.lista_carros.remove(carro_existente)

                    opcao_voltar()


            else:
                print("Dados do usuário escolhido não conferem. Por favor, tente novamente")

    elif opcao == 4:
        codigo_reserva_usr = int(input("Por favor, digite o código da sua reserva: "))
        reserva_existente = next(reserva for reserva in Reserva.lista_reservas if reserva.codigo_da_reserva == codigo_reserva_usr)

        if reserva_existente is not None:
            Reserva.detalhes_reserva(reserva_existente)
        else:
            print("""
            Não possuimos uma reserva com esse código. Você será redirecionado para a nossa tela inicial.
            """)    

        tela_inicial()

    elif opcao == 5:
        print("-------------------------------------\n")
        print("-------Cadastro de Veículo de Locação-----------\n")    
        print("Olá, seja bem vinda à área de cadastro de cliente da ACME RentACar")
    
        veiculo = VeiculoLocacao.cadastro_carro()
        veiculo.detalhes()
        VeiculoLocacao.lista_carros.append(veiculo)

        print("""
        Veículo adicionado à nossa lista de locação.
        Você está sendo redirecionada para o nosso painel de opções.
        """)

        return VeiculoLocacao.lista_carros, tela_inicial()


    else:
        print("Por favor, escolha uma opção entre 1 a 6: ")
