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
    """)

    opcao = int(input("Por favor, digite a opção desejada dentre as disponibilizadas acima: "))

    escolha_usuario(opcao)

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

def escolha_usuario(opcao):
    if opcao == 1:
        print("-------------------------------------\n")
        print("-------Cadastro de Cliente-----------\n")    
        print("Olá, seja bem vinda à área de cadastro de cliente da locadora de carros ACME")
    
        cliente = Cliente.cadastro_cliente()
        cliente.detalhes()
        Cliente.lista_clientes.append(cliente)

        print("""
        Muito obrigada por fazer o seu cadastro de cliente. Seja bem vinda à ACME!
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
            print(user)

            print(Cliente.lista_clientes)
            print(lista_usuarios)

            # usuario_existente = filter(lambda x: x.usuario == user, Cliente.lista_clientes)
            usuario_existente = next(cliente for cliente in Cliente.lista_clientes if cliente.usuario == user)


            print(f"procura: {usuario_existente}")

            if usuario_existente.usuario == user:
                carro_escolhido = int(input("Por favor, digite o código do carro escolhido"))
                carro_existente = next(carro for carro in VeiculoLocacao.lista_carros if carro.codigo_do_carro == carro_escolhido)

                if carro_existente is not None:
                    Reserva.montar_reserva(reserva.codigo_da_reserva,usuario_existente.usuario,carro_existente) 
                    VeiculoLocacao.lista_carros.remove(carro_existente)

                    opcao_voltar()


            else:
                print("Dados do usuário escolhido não conferem. Por favor, tente novamente")

    else:
        print("Por favor, escolha uma opção entre 1 a 3")
