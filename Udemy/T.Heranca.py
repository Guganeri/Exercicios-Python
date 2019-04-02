from builtins import object

class animal(object):
    def __init__(self):
        print('Animal Criado')

    def quemSouEu(self):
        print('Eu sou um animal')

    def comer(self):
        print('Comendo...')

class Cachorro(animal):
    def __init__(self):
        animal.__init__(self)
        print('Cachorro criado.')

    def quemSouEu(self):
        print('Eu sou um cachorro')
    def latir(self):
        print('Au au.')

sam = Cachorro()
