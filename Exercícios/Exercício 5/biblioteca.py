from parte_5 import Livro

#6)No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro_biblioteca = Livro('Percy Jackson', 'Rick Riordan', 2005)
print(f'{livro_biblioteca.titulo} está disponível? {livro_biblioteca.status()}')
livro_biblioteca.emprestar()
print(f'{livro_biblioteca.titulo} está disponível? {livro_biblioteca.status()}')

#7)No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
livro_biblioteca1 = Livro('Eragon', 'Christopher Paolini', 2002)
livro_biblioteca2 = Livro('1984', 'George Orwell', 1949)

ano = int(input('Digite o ano: '))
Livro.verificar_disponibilidade(ano)

