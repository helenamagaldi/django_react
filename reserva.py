import random

from carro import VeiculoLocacao
from pessoa import Pessoa

class Reserva(Pessoa, VeiculoLocacao):
  
    def __init__(self, codigo_da_reserva, usuario):
      self.codigo_da_reserva = codigo_da_reserva
      self.usuario = usuario 

    @classmethod
    def fazer_reserva(self):
      codigo_da_reserva = random.randint(0,10)
      usuario = input("Por favor, digite o seu nome de usuário")

      return self(codigo_da_reserva, usuario)