import os
os.system('cls')

class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'A conta pertence a {self._titular} e possui saldo igual a R${self._saldo:.2f}'
        
    def status(self):
        return 'Ativada' if self._ativo else 'Desativada'

    @classmethod
    def ativar_conta(cls, conta):
            conta._ativo = True

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

conta1 = ContaBancaria('João', 1000)
conta2 = ContaBancaria('Maria', 500)

print(conta1)
print(conta2)
print()
conta3 = ContaBancaria('Carlos', 200)

print(f'Antes de ativar: Conta ativa? {conta3.status()}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: Conta ativa? {conta3.status()}')

conta4 = ContaBancaria('Fernanda', 1500)
print(f'\n{conta4}')


class ClienteBanco:
    def __init__(self, nome, profissao, endereco, idade = 0, cpf = 0,):
        self._nome = nome
        self._profissao = profissao
        self._endereco = endereco
        self._idade = idade
        self._cpf = cpf

    @classmethod
    def criar_conta(cls, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        return conta

cliente1 = ('Ana', 'Advogada', 'Xique-Xique, Bahia', 18, 123123123.12)
cliente2 = ('Arnaldo', 'Caçador', 'Rio de Janvier, Presídio', 64, 321321321.21)
cliente3 = ('Chifon', 'Desenhista', 'Juan Pablo, Poluição', 42, 543345453.35)

cliente4 = ClienteBanco.criar_conta('José', 1000000)
print(f'Conta de {cliente4.titular} criada com saldo inicial de R${cliente4.saldo:.2f}\n')
print(cliente4)