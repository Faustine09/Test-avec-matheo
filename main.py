from class_objet import *

calcul = Calculette()
calcul.afficher()
fermer = False

clic = calcul.recupClic()
while not fermer:
    if 50 <= clic.x <= 315 and 200 <= clic.y <= 560:
        nb = calcul.nombre(clic)
        if nb != None and nb != -1:
            calcul.afficherNb(nb)
            clic = calcul.recupClic()
        elif nb == -1:
            calcul.enter(clic)
            clic = calcul.recupClic()
            calcul.supr()
    elif 385 <= clic.x <= 505 and 205 <= clic.y <= 465:
        op = calcul.operateur(clic)
        if op != None and op != "AC":
            calcul.afficherOp(op)
        elif op == "AC":
            calcul.supr()
        clic = calcul.recupClic()
    elif clic.x >= 570 and clic.y <= 30:
        fermer = True

calcul.fermer()
