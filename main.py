from class_objet import *

calcul = Calculette()
calcul.afficher()
clic = None

while not calcul.fermerBool():
    clic = calcul.recupClic()
    if 50 <= clic.x <= 315 and 200 <= clic.y <= 560:
        nb = calcul.nombre(clic)
        if nb != None and nb != -1:
            calcul.afficherNb(nb)
        elif nb == -1:
            calcul.enter(clic)
    if 385 <= clic.x <= 505 and 205 <= clic.y <= 465:
        op = calcul.operateur(clic)
        if op != None:
            calcul.afficherOp(op)


calcul.fermer()