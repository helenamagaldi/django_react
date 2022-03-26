from datetime import datetime, date
import random

from carro import VeiculoLocacao
from cliente import Cliente

class Reserva:
    lista_reservas = []
  
    def __init__(self, codigo_da_reserva, usuario, data_inicio, data_fim, duracao_reserva):
      self.codigo_da_reserva = codigo_da_reserva
      self.usuario = usuario 
      self.data_inicio = data_inicio
      self.data_fim = data_fim
      self.duracao_reserva = duracao_reserva

      self.lista_reservas.append(self)


    @classmethod
    def requisitar_reserva(self):
      codigo_da_reserva = random.randint(0,10)
      usuario = input("Por favor, digite o seu nome de usuário: ")
      data_inicio = input("Início do período do aluguel do veículo (Formato DD/MM/AAAA): ")
      datetime_inicio = datetime.strptime(data_inicio, "%d/%m/%Y").date()
      data_fim = input("Fim do período do aluguel do veículo (Formato DD/MM/AAAA): ")
      datetime_fim = datetime.strptime(data_fim, "%d/%m/%Y").date()

      duracao_reserva = (datetime_fim-datetime_inicio).days

      return self(codigo_da_reserva, usuario, data_inicio, data_fim, duracao_reserva)

    @classmethod
    def montar_reserva(self, codigo_da_reserva, usuario_existente, carro_escolhido):
        print("""
        Reserva realizada com sucesso!
        Por favor, anote o código da sua reserva :)
        """)
        print(f"Código da reserva: {codigo_da_reserva}, Usuário: {usuario_existente}, Carro Escolhido: {carro_escolhido.modelo}, {carro_escolhido.marca}, {carro_escolhido.placa}")

        return self

    @classmethod
    def detalhes_reserva(self, reserva_existente):

        print("--------------")
        print("-- Reserva de Automóvel ou Similar - ACME RentACar --")
        print(f"Usuário: {reserva_existente.usuario}")
        print(f"Código da reserva: {reserva_existente.codigo_da_reserva}")
        print(f"Data Início: {reserva_existente.data_inicio}")
        print(f"Data Fim: {reserva_existente.data_fim}")
        print(f"Duração da reserva: {reserva_existente.duracao_reserva} dias")
        print("--------------")


