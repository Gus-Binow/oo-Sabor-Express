import os
os.system('cls')

class Carro:
    def __init__(self, modelo, cor, ano=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

fiat = Carro('Uno', 'Cinza', 2001)
print(fiat)

class Restaurante:
    def __init__(self, nome, preco, tempo, categoria):
        self.nome = nome
        self.preco = preco
        self.tempo = tempo
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.preco} | {self.tempo} | {self.categoria} | {self.ativo}'
    
japones = Restaurante('Hokkaido', 'Mediano', '60 Minutos', 'Rodízio')
print(japones)

class Cliente:
    def __init__(self, nome, gen, idade = 0, telefone = 0):
        self.nome = nome
        self.gen = gen
        self.idade = idade
        self.telefone = telefone
    
    def __str__(self):
        return f'{self.nome} | {self.gen} | {self.idade} | {self.telefone}'

cliente1 = Cliente('Gustavo', 'Masculino', 24, 999020102)
print(cliente1)