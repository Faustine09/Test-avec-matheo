from tkiteasy import *

class Calculette():

    def __init__(self, a=None, b = None):
        self.__a = a
        self.__b = b
        self.__chiffres = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
        self.__operateurs = [["+", "AC"], ["-", "exp"], ["x", "F"], ["÷", "1e"]]

    def addition(self):
        return self.__a + self.__b

    def soustraction(self):
        return self.__a-self.__b

    def multiplication(self):
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
        resultat = 1
        term = 1
        for i in range (1,4) :
            term *= self.__a /i
            resultat += term
        return resultat


    def fibonacci(self):
        if self.__a == 0 or self.__a == 1 :
            return True
        else :
            a = 0
            b = 1
            while True :
                c = a + b
                if c == self.__a :
                    return True
                elif c > self.__a :
                    return False
                else :
                    a = b
                    b = c


    def nbpremier(self):
        if self.__a <= 1 :
            return False
        else:
            premier = True
            for i in range(2, self.__a):
                multiple = i
                while multiple <= self.__a:
                    if multiple == self.__a:
                        premier = False
                        break
                    multiple = multiple + i
                if not premier:
                    break
        return premier

    def supr (self) :
        pass

    def __str__(self):
        self.__g = ouvrirFenetre(600, 600)
        self.__g.dessinerRectangle(50, 50, 500, 100, "lavenderblush")
        for i in range(3):
            for j in range(3):
                self.__g.dessinerRectangle(50+i*95, 200+j*95, 75, 75, "lavenderblush")
                self.__g.afficherTexte(self.__chiffres[j][i], 87.5+i*95, 237.5+j*95, "darkblue", 24)
        self.__g.dessinerRectangle(50, 485, 75, 75, "lavenderblush")
        self.__g.dessinerRectangle(145, 485, 170, 75, "lavenderblush")
        self.__g.afficherTexte("0", 87.5, 522.5, "darkblue", 24)
        self.__g.afficherTexte("Enter", 230, 522.5, "darkblue", 24)

        for i in range(2):
            for j in range(4):
                self.__g.dessinerRectangle(385+i*70, 205+j*70, 50, 50, "lavenderblush")
                self.__g.afficherTexte(self.__operateurs[j][i], 410+i*70, 230+j*70, "darkblue", 18)



        self.__g.attendreClic()
        self.__g.fermerFenetre()
        return


calcul = Calculette()
print(calcul)