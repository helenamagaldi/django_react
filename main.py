import datetime

from carro import VeiculoLocacao
from script import tela_inicial
from cliente import Cliente
from reserva import Reserva
 
 
def main():
    time = datetime.datetime.now()

    carro1 = VeiculoLocacao("Creta", "Hyundai", "SUV", "Manual", "Gasolina", "2003", "AAA-1111", 111)
    carro2 = VeiculoLocacao("Marea", "Fiat", "Wagon", "Automatico", "gasolina", "2005", "BBB-2222", 222)
    carro3 = VeiculoLocacao("Gol", "Volkswagen", "Popular", "Automatico", "flex", "2012", "CCC-3333", 333)

    cliente1 = Cliente("cookie", "Cookie Monster", "1234", "1234")
    cliente2 = Cliente("aladin", "Aladin The King", "0987", "0987")
    cliente3 = Cliente("cesar", "Cesar Labs", "2424", "2424")


    tela_inicial()

if __name__ == "__main__":
    main()