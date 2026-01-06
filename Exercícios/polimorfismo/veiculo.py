from abc import ABC, abstractmethod

#Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
class Veiculo(ABC):
    #No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

#Crie uma nova classe chamada Carro que herda da classe Veiculo.
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        #No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        return f"O carro {self.marca} {self.modelo} está ligado."

    def __str__(self):
        return f"Marca: {self.marca.ljust(25)} | Modelo: {self.modelo.ljust(25)} | Cor: {self.cor}"