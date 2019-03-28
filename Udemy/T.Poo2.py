class Circulo(object):
    pi = 3.14

    def __init__(self, raio=1):
        self.raio = raio

    def area(self):
        return self.raio ** 2 * self.pi

    def defRaio(self, raio):
        self.raio = raio

    def obtemRaio(self):
        return self.raio


c = Circulo(2)
print(c.area())
c.defRaio(3)
print(c.raio)

d = Circulo(5)
print(c.area())
d.defRaio(5)
print(d.raio)