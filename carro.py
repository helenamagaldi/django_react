class Carro(object):
  
    def __init__(self, modelo, marca, categoria, transmissao, combustivel):
        self.modelo = modelo
        self.marca = marca
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel

    def detalhes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Categoria: {self.categoria}")
        print(f"Tipo de transmissão: {self.transmissao}")
        print(f"Tipo de combustível: {self.combustivel}")

      
      
class VeiculoLocacao(Carro):
    lista_carros = []

    def __init__(self, modelo, marca, categoria, transmissao, combustivel, ano, placa, codigo_do_carro):
        self.ano = ano
        self.placa = placa
        self.codigo_do_carro = codigo_do_carro
  
        Carro.__init__(self, modelo, marca, categoria, transmissao, combustivel)

        self.lista_carros.append(self)

    @classmethod
    def cadastro_carro(self):
      modelo = input("Por favor, digite o modelo do veículo de locação: ")
      marca = input("Por favor, digite a marca do veículo de locação: ")
      categoria = input("Por favor, digite a categoria do veículo de locação: ")
      transmissao = input("Por favor, digite o tipo de transmissão do veículo de locação: ")
      combustivel = input("Por favor, digite o tipo de combustivel do veículo de locação: ")
      ano = input("Por favor, digite o ano do veículo de locação: ")
      placa = input("Por favor, digite a placa do veículo de locação: ")
      codigo_do_carro = int(input("Por favor, digite o código do veículo de locação: "))

      return self(modelo, marca, categoria, transmissao, combustivel, ano, placa, codigo_do_carro)
          
    def detalhes(self):
        print("--------------")
        print("-- Cadastro de Carro Atualizado --")
        print(f"Codigo do carro de aluguel: {self.codigo_do_carro}")
        print(f"Ano: {self.ano}")
        print(f"Placa: {self.placa}")
        print("--------------")
        print(Carro.detalhes(self))