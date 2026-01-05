import os
os.system('cls')

class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade
    
class Pessoa:
    def __init__(self, nome, profissao, idade = 0):
        self._nome = nome
        self._profissao = profissao
        self._idade = idade

    def __str__(self):
        return f'{self._nome} | {self._profissao} | {self._idade} anos.'
    
    def aniversario(self):
        self._idade += 1
    
    @property
    def saudacao(self):
        return f'Bem vindo, {self._nome}, nobre {self._profissao}! Que seu conhecimento em sua área ajude a tornar o mundo um lugar melhor!'
    
pessoa1 = Pessoa(nome = 'Gustavo', profissao = 'Estudante', idade = 24)

print(pessoa1)

pessoa1.aniversario()
print(pessoa1)

print(pessoa1.saudacao)