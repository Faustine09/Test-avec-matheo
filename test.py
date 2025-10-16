from tkiteasy import *

class Calculette():

    def __init__(self, a=None, b = None):
        self.__a = a
        self.__b = b

    def addition(self):
        return self.a + self.b

    def soustraction(self):
        return self.a-self.b

    def mutliplication(self):
        resultat = 0
        for i in range (self.b) :
            resultat += self.a
        return resultat


    def division(self):
        pass

    def exponentielle(self):
        pass

    def fibonacci(self):
        pass

    def nbpremier(self):
        pass

    def __str__(self):
        self.__g = ouvrirFenetre(800, 600)
        self.__g.dessinerRectangle(50, 50, 500, 100, "white")
        self.__g.attendreClic()
        self.__g.fermerFenetre()
        return


calcul = calculette()
print(calcul)