class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return (
            f'Marca: {self.marca}\n'
            f'Modelo: {self.modelo}\n'
            f'Status: {'Ligado' if self._ligado else 'Desligado'}'
        )
    
#-------------------------------------------------------------------------#

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca,modelo)
        self.portas = portas

    def __str__(self):
        str_pai = super().__str__()
        return f'{str_pai}\n' f'Portas: {self.portas}\n'
    
#-------------------------------------------------------------------------#


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def __str__(self):
        str_1 = super().__str__()
        return f'{str_1}\n' f'Tipo: {self.tipo}\n'