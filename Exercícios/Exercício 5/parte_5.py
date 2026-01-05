import os
os.system('cls')

#1)Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    biblioteca = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo.title()
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.biblioteca.append(self)


#2)Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'{self.titulo}, obra de {self.autor} | Publicado em {self.ano_publicacao}\n'
    

#3)Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self.disponivel = False
        return 'Indisponível'
    
    def status(self):
        return 'Disponível' if self.disponivel else 'Indisponível'
    

#4)Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    def verificar_disponibilidade(ano):
        livros_disponiveis = []

        for livro in Livro.biblioteca:
            if livro.ano_publicacao == ano and livro.disponivel:
                livros_disponiveis.append(livro)

        if livros_disponiveis:
            print(f'\nLivros disponíveis publicados em {ano}:')
            for i, livro in enumerate(livros_disponiveis, 1):
                print(f'{i} - {livro}')
        else:
            print('Não há livros desse ano disponíveis!')



if __name__ == '__main__':
    #print do exercício 2
    livro1 = Livro('Eragon', 'Christopher Paolini', 2002)
    livro2 = Livro('1984', 'George Orwell', 1949)

    print(livro1)
    print(livro2)


    #print do exercício 3
    livro3 = Livro('As crônicas de Nárnia', 'C. S. Lewis', 1950)
    print(f'{livro3.titulo} está disponível? {livro3.status()}')
    livro3.emprestar()
    print(f'{livro3.titulo} está disponível? {livro3.status()}')

    #busca e print do exercício 4
    ano = int(input('\n\nQuer buscar livros de qual ano? '))
    Livro.verificar_disponibilidade(ano)

   