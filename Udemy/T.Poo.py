class Dog(object):
    species='mamifero'

    def __init__(self,raça):
        self.raça = raça
        print(len(self.species))

    def latir(self):
        print('Au au')

sam = Dog(raça='Beagle')
sam.latir()