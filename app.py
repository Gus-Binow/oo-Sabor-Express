from modelos.restaurante import Restaurante
import os
os.system('cls')

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_availiacao('Gui', 10)
restaurante_praca.receber_availiacao('Lais', 8)
restaurante_praca.receber_availiacao('Emy', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
