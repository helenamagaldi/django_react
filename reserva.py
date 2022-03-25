import random

from carro import VeiculoLocacao
from pessoa import Pessoa

class Reserva:
  
    def __init__(self, codigo_da_reserva, usuario):
      self.codigo_da_reserva = codigo_da_reserva
      self.usuario = usuario 

    @classmethod
    def requisitar_reserva(self):
      codigo_da_reserva = random.randint(0,10)
      usuario = input("Por favor, digite o seu nome de usuário")

      return self(codigo_da_reserva, usuario)

    @classmethod
    def montar_reserva(self, codigo_da_reserva, usuario_existente, carro_escolhido):
        print("""
        Reserva realizada com sucesso!
        """)
        print(f"Código da reserva: {codigo_da_reserva}, Usuário: {usuario_existente}, Carro Escolhido: {carro_escolhido.modelo}, {carro_escolhido.marca}, {carro_escolhido.placa}")

    @classmethod
    def detalhes_reserva(self):
        print("dtalhes reserva")