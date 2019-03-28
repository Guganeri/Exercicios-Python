class Animal(object):
    def __init__(self):
        print('Animal criado')

    def quemSouEu(self):
        print('Eu sou um animal')
    def comer(self):
        print('comendo...')

animal = Animal()
print(animal.comer())
print(animal.quemSouEu())

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criado')
    def qeumSoueu(self):
        print('Sou um cachorrro')
    def latir(self):
        print('Au au')


print(sam = Cachorro())
