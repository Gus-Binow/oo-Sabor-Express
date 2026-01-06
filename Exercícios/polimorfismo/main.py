#Em um arquivo chamado main.py, importe a classe Carro.
from veiculo import Carro

#No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
carro1 = Carro('Mitsubishi', 'Eclipse', 'Preto')
carro2 = Carro('Porsche', '911', 'Branco')
carro3 = Carro('Honda', 'Civic', 'Prata')

print(carro1, carro2, carro3, sep="\n")