from tkiteasy import *

class calculette():

    def __init__(self):
        pass

    def addition(self):
        pass

    def soustraction(self):
        pass

    def mutliplication(self):
        pass

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