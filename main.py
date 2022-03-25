import datetime

from carro import VeiculoLocacao
from helpers import escolha_usuario, tela_inicial
from pessoa import Pessoa
from reserva import Reserva
 
 
def main():
    carro1 = VeiculoLocacao("Palio", "Fiat", "popular", "manual", "gasolina", "2003", "AAA-1111", 111)
    carro2 = VeiculoLocacao("Marea", "Fiat", "wagon", "automatico", "gasolina", "2005", "BBB-2222", 222)
    carro3 = VeiculoLocacao("Gol", "Volkswagen", "popular", "automatico", "flex", "2012", "CCC-3333", 333)

    time = datetime.datetime.now()

    tela_inicial()

    # print("Bem vindo à locadora de carros ACME!\n")
    # print("-------------------------------------\n")

    # print("""
    # 1. Cadastro de Cliente
    # 2. Lista de carros disponíveis
    # 3. Fazer Reserva
    # """)

    # opcao = int(input("Por favor, digite a opção desejada dentre as disponibilizadas acima: "))

    # escolha_usuario(opcao)

if __name__ == "__main__":
    main()