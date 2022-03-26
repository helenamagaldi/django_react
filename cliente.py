class Cliente(object):
    lista_clientes = []

    def __init__(self, nome, cpf, rg, usuario):
      self.usuario = usuario
      self.nome = nome
      self.cpf = cpf
      self.rg = rg

      self.lista_clientes.append(self)


    @classmethod
    def cadastro_cliente(self):
      usuario = input("Por favor, digite um nome de usuário: ")
      nome = input("Por favor, digite o seu nome: ")
      cpf = input("Por favor, digite o seu CPF: ")
      rg = input("Por favor, digite o seu RG: ")

      return self(usuario, nome, cpf, rg)

    def detalhes(self):
        print("--------------")
        print("-- Cadastro de Cliente Atualizado --")
        print(f"Usuário: {self.usuario}")
        print(f"Nome completo: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"RG: {self.rg}")
        print("--------------")