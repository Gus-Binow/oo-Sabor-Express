from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

import os
os.system('cls')

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade!')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
