import os
os.system('cls')

class Musica:
    playlist = []

    def __init__(self, nome, artista, duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.playlist.append(self)

    def mostra_playlist():
        for music in Musica.playlist:
            print(f'{music.nome} | {music.artista} | {music.duracao}')
    
mulan = Musica('I`ll make a Man Out of You', 'Peyton Parrish', 189)
TEHC = Musica('Hotel California', 'Eagles', 390)

Musica.mostra_playlist()