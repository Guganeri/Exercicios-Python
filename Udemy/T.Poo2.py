class Circulo(object):
    pi = 3.14

    def _init_(self, raio=1):
        self.raio = raio

    def area(self):
        return self.raio **2 * self.pi

    def defRaio(self, raio):
        self.raio = raio

    def obtemRaio(self):
        return self.raio

c = Circulo
