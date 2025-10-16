from tkiteasy import *

class Calculette():

    def __init__(self, a=None, b = None):
        self.__a = a
        self.__b = b

    def addition(self):
        return self.__a + self.__b

    def soustraction(self):
        return self.__a-self.__b

    def mutliplication(self):
        resultat = 0
        for i in range (self.__b) :
            resultat += self.__a
        return resultat


    def division(self):
        a = self.__a
        b = self.__b
        resultat = 0
        if b != 0 :
            while  a >= b :
                a -= b
                resultat += 1
            a = self.multiplication(a,10)
            while a >= b :
                a -= b
                resultat += 0.1
            a = self.multiplication (a,10)
            while a >= b :
                a -= b
                resultat += 0.01
        else :
            return None
        return resultat

    def exponentielle(self):
        pass

    def fibonacci(self):
        pass

    def nbpremier(self):
        pass
    def supr (self) :
        pass
    def __str__(self):
        self.__g = ouvrirFenetre(800, 600)
        self.__g.dessinerRectangle(50, 50, 500, 100, "white")
        self.__g.attendreClic()
        self.__g.fermerFenetre()
        return


calcul = Calculette()
print(calcul)