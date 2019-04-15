class Book(object):
    def __init__(self, titulo, autor, paginas):
        print('Um livro foi criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return "Titulo {a}".format(a=self.titulo)

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Livro Destruido')

livro1 = Book('Pyhton', 'Gustavo',100)
print(len(livro1))
