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
        self.codigo_do_carro = codigo_do_carro
        self.ano = ano
        self.placa = placa
  
        Carro.__init__(self, modelo, marca, categoria, transmissao, combustivel)

        self.lista_carros.append(self)
          
    def detalhes(self):
        print("--------------")
        print("-- Cadastro de Carro Atualizado --")
        print(f"Codigo do carro de aluguel: {self.codigo_do_carro}")
        print(f"Ano: {self.ano}")
        print(f"Placa: {self.placa}")
        print("--------------")
        print(Carro.detalhes(self))