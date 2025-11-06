from tkiteasy import *

class Calculette():

    def __init__(self,):
        self.__a = None
        self.__b = None
        self.__chiffres = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
        self.__operateurs = [["+", "AC"], ["-", "exp"], ["x", "F"], ["÷", "1e"]]
        self.__op = None
        self.__opBool = False
        self.__txt = None

    def addition(self):
        return self.__a + self.__b

    def soustraction(self):
        return self.__a - self.__b

    def multiplication(self):
        resultat = 0
        for i in range (self.__b) :
            resultat += self.__a
        return resultat

    def multiplication2(self,a,b):
        resultat = 0
        for i in range(b):
            resultat += a
        return resultat

    def division(self):
        a = self.__a
        b = self.__b
        resultat = 0
        if b != 0 :
            while  a >= b :
                a -= b
                resultat += 1
            a = self.multiplication2(a,10)
            while a >= b :
                a -= b
                resultat += 0.1
            a = self.multiplication2(a,10)
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
        self.__g.supprimer(self.__objtxt)
        self.__objtxt = self.__g.afficherTexte("", 300, 100, "darkblue", 24)
        self.__a = None
        self.__b = None
        self.__op = None
        self.__opBool = False
        self.__txt = None
        return

    def afficher(self):
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
        self.__g.dessinerLigne(590, 10, 570, 30, "red", 6)
        self.__g.dessinerLigne(570, 10, 590, 30, "red", 6)

        for i in range(2):
            for j in range(4):
                self.__g.dessinerRectangle(385+i*70, 205+j*70, 50, 50, "lavenderblush")
                self.__g.afficherTexte(self.__operateurs[j][i], 410+i*70, 230+j*70, "darkblue", 18)

        self.__objtxt = self.__g.afficherTexte("", 300, 100, "darkblue", 24)


    def fermer(self):
        self.__g.fermerFenetre()

    def recupClic(self):
        return self.__g.attendreClic()

    def nombre(self, clic):
        j = (clic.x - 50) // 95
        i = (clic.y - 200) // 95
        if i <= 2:
            if (clic.x - 50) % 95 < 75 and (clic.y - 200) % 95 < 75:
                return self.__chiffres[i][j]
        elif j == 0 and (clic.x - 50) % 95 < 75:
            return "0"
        elif j == 1 or j == 2 :
            return -1
        return None

    def operateur(self, clic):
        j = (clic.x - 385) // 70
        i = (clic.y - 205) // 70
        if (clic.x - 385) % 70 < 50 and (clic.y - 205) % 70 < 50:
            return self.__operateurs[i][j]

    def afficherNb(self, nb):
        self.__g.supprimer(self.__objtxt)
        if not self.__opBool:
            if self.__a is not None :
                self.__a += str(nb)
            else:
                self.__a = str(nb)
        else:
            if self.__b is not None :
                self.__b += str(nb)
            else:
                self.__b = str(nb)
        if self.__txt is not None:
            self.__txt += str(nb)
        else:
            self.__txt = str(nb)
        self.__objtxt = self.__g.afficherTexte(self.__txt, 300, 100, "darkblue", 24)
        self.__g.actualiser()

    def afficherOp(self, op):
         if not self.__opBool:
            self.__g.supprimer(self.__objtxt)
            self.__op = op
            self.__txt = self.__txt + (f" {self.__op} ")
            self.__opBool = True
            self.__objtxt = self.__g.afficherTexte(self.__txt, 300, 100, "darkblue", 24)
            self.__g.actualiser()

    def enter(self, clic):
        self.__a = int(self.__a)
        if self.__b is not None :
            self.__b = int(self.__b)

        if self.__op == "+":
            result = self.addition()
        elif self.__op == "-":
            result = self.soustraction()
        elif self.__op == "x":
            result = self.multiplication()
        elif self.__op == "÷":
            result = self.division()
        elif self.__op == "exp":
            result = self.exponentielle()
        elif self.__op == "F":
            result = self.fibonacci()
        elif self.__op == "1e":
            result = self.nbpremier()
        else:
            self.supr()
            return

        self.__g.supprimer(self.__objtxt)
        self.__objtxt = self.__g.afficherTexte(str(result), 300, 100, "darkblue", 24)
        self.__g.actualiser()
        return
