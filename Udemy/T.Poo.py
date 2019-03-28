class Dog(object):
    species='mamifero'

    def __init__(self,raça):
        self.raça = raça
        print(len(self.species))

sam = Dog(raça='Beagle')