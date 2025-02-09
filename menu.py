#fichier fait par Elazar
from fltk import * 
from pathlib import Path
from V1 import *

def menu_principal(): 
    """on affiche le meu principal avec tout les choix du menu (gere un peu tout le menu)
    param: aucun 
     --> return None  """ 
    from V2 import def_var,main
    while True:
        efface_tout()
        affichage_principal()
        mise_a_jour()
        ev = donne_ev()
        ty = type_ev(ev)
        nb_j = 0

        if ty == "Quitte":
            ferme_fenetre()
            exit(0)

        elif ty == "ClicGauche":
            x = abscisse(ev)
            y = ordonnee(ev)
            # lance le jeu (jouer) 
            if 50 < x < 300 and 50 < y < 130:
                efface_tout()
                taille_fenetre,taille_case,lst_decalage ,languette_H, languette_V,lst_bille_supr,grille,nb_j_ordi,continuer,nb_j ,nb_coup,nb_joueur_coup,posit_languette_H, posit_languette_V = def_var()
                main(taille_fenetre,taille_case,lst_decalage ,languette_H, languette_V,lst_bille_supr,grille,nb_j_ordi,continuer,nb_j ,nb_coup,nb_joueur_coup,posit_languette_H, posit_languette_V)
              
            # rejouer
            elif 500<x<750 and 50<y<130:
                efface_tout()
                taille_fenetre,taille_case,lst_decalage ,languette_H, languette_V,lst_bille_supr,grille,nb_j_ordi,continuer,nb_j ,nb_coup,nb_joueur_coup,posit_languette_H, posit_languette_V,= def_var()
                main(taille_fenetre,taille_case,lst_decalage ,languette_H, languette_V,lst_bille_supr,grille,nb_j_ordi,continuer,nb_j ,nb_coup,nb_joueur_coup,posit_languette_H, posit_languette_V)
            #quitte le jeu 
            elif 50<x<300 and 610<y<690:
                ferme_fenetre()
                exit(0)
            # choisir entre bille aleatoire ou placer soit meme les billes
            elif 50<x<300 and 330<y<410:
                choix_bille = m_bille()
                ecrire_fichier(choix_bille,"menu_bille.txt")
            #nb de joueur et le stock dans un fichier (nb_joueur)
            elif 500 < x < 750 and 330<y<410:
                nb_j = nb_joueur() 
                ecrire_fichier(str(nb_j),"nb_joueur.txt")
            #regle 
            elif 500< x< 750 and 610 <y<690:
                regle()
        mise_a_jour()
    efface_tout()

def affichage_principal():
    """ affiche le menu principal 
    param :aucun
    --> return None"""
    largeur_rectangle = 250
    hauteur_rectangle = 80

    espacement_horizontal = 80
    espacement_vertical = 50

    espacement_horizontal = 200 
    espacement_vertical = 200
    rectangle(0, 0, 800, 800, remplissage="skyblue")

    x, y = 50, 50
    for i in range(3):
        for j in range(4,6):
            rectangle(x, y, x + largeur_rectangle, y + hauteur_rectangle,remplissage = "red")
            x += largeur_rectangle + espacement_horizontal
        x = 50
        y += hauteur_rectangle + espacement_vertical
    texte(175,90,"JOUER",ancrage = "center")
    texte(625,370,"NB JOUEUR",ancrage = "center")
    texte (175,650,"QUITTER",ancrage = "center")
    texte(175,370,"BILLE",ancrage = "center")
    texte(625,90,"REJOUER",ancrage = "center")
    texte(625,650,"REGLE",ancrage = "center")

def lire_fichier(fichier): 
    """lis le fichier recu en param et renvoie le contenu sinon None
    param : fichier : le fichier qu'on veut lire(fichier.txt) 
    --> return contenu du fichier 
    """
    try :
        with open(str(fichier),"r") as r: 
            contenu = r.read()
        return contenu
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'existe pas.")
        return None

def nb_joueur():
    """affiche une nouvelle fenetre pour choisir ou changer le nb de joueur et si on active l'IA (ecrit direct dans un fichier)
    param: aucun 
    --> return le nb de joueur (int) """
    ferme_fenetre()
    cree_fenetre(800,800)
    while True:
        ev = donne_ev()
        ty = type_ev(ev)
        x2,y2,l= 200,300,50
        nb_j = int(lire_fichier("nb_joueur.txt"))
        ia_yes_or_no = lire_fichier("IA.txt")
        #affiche la fenetre
        rectangle(0, 0, 800, 800, remplissage="skyblue")
        rectangle(200,20,600,100)
        texte(400,60,"NB JOUEUR",ancrage = "center")
        # affiche si on active l,IA
        rectangle(300,450,500,550)
        texte(400,470,"IA",ancrage= "center")
        if ia_yes_or_no == "ON":
            rectangle(345,500,395,525,remplissage = "green")
        elif ia_yes_or_no == "OFF":
            rectangle(415,500,465,525,remplissage = "green")
        x3 = 345
        for i in range(2):
            rectangle(x3,500,x3+50,525)
            x3+=70
        texte(370,512.5,"ON",taille = "10",ancrage = "center")
        texte(440,512.5,"OFF",taille = "10",ancrage = "center")
        
        for i in range(4): # affiche 4 carre pour les chiffres
            if nb_j == i+1:
                rectangle(x2 -10 , y2-10 ,x2+l+10,y2+l+10 ,remplissage="purple")
            rectangle(x2,y2,x2+l,y2+l,remplissage = "blue") 
            texte(x2,y2,f"{i+1}")
            x2 +=100  
        retour_menu()
        mise_a_jour()
        if ty =="Quitte": 
            ferme_fenetre()
            exit(0)
        # choix du nb joueur 
        elif ty == "ClicGauche":
            x = abscisse(ev)
            y = ordonnee(ev)
            if 200 < x < 250 and 300 < y < 350:
                return 1
            elif 300 < x < 350 and 300 < y < 350:
                return 2 
            elif 400 < x< 450 and 300 < y < 350: 
                return 3 
            elif 500 < x < 550 and 300 < y < 350: 
                return 4
            elif 345<x<395 and 500<y<525:
                ecrire_fichier("ON","IA.txt")
            elif 415<x< 465 and 500<y<525:
                ecrire_fichier("OFF","IA.txt")

def ecrire_fichier(valeur,fichier):
    """ecrit dans un fichier un valeur pour la stocker
    params:  valeur: la valeur a stocket
            fichier : le nom du fichier ou le chemin relatif
    return None 
    """
    with open(fichier,"w") as f: 
        contenu = f.write(valeur)

def retour_menu(): 
    """affiche un petit rectangle en haut a droite pour retourner automatiquement au menu principal 
    param :aucun 
    --> return None """
    rectangle(5,5,100,50,remplissage="blue",tag = "M")
    texte(52,27.5,"MENU",ancrage="center",couleur="tan",tag = "M")
    ev = donne_ev()
    ty = type_ev(ev)
    if ty == "Quitte":
        ferme_fenetre()
        exit(0)
    elif ty =="ClicGauche":
        x = abscisse(ev)
        y = ordonnee(ev)
        # si on clique tout en haut a gauche
        if 5 <= x <= 100 and 5 <= y <= 50:
            menu_principal()
    mise_a_jour()


def m_bille():
    """fonction du menu pour choisir si on veut placer les billes ou mettre les billes aleatoirement
    param : aucun 
    return :None"""
    ferme_fenetre()
    cree_fenetre(800,800)
    while True:
        # variable utiliser dans la fonction 
        ev = donne_ev()
        ty = type_ev(ev)
        x_cercle1 = 200
        x_cercle2 = 600
        y_cercle = 300
        rayon_cercle = 100
        choix_bille = lire_fichier("menu_bille.txt")
        # affiche la fenetre
        rectangle(0, 0, 800, 800, remplissage="skyblue")
        if choix_bille == "aleatoire": 
            rectangle(x_cercle1-100,y_cercle-20,x_cercle1+100,y_cercle+20,remplissage = "green")
        elif choix_bille == "manuel": 
            rectangle(x_cercle2-100,y_cercle-20,x_cercle2+100,y_cercle+20,remplissage = "green")
        cercle(x_cercle1,y_cercle,rayon_cercle)
        texte(x_cercle1,y_cercle,"aleatoire",ancrage="center")
        cercle(x_cercle2,y_cercle,rayon_cercle)
        texte(x_cercle2,y_cercle,"pose manuel",ancrage= "center")
        retour_menu()
        mise_a_jour()

        if ty == "Quitte": 
            ferme_fenetre()
            exit(0)
        elif ty == "ClicGauche":
            x = abscisse(ev) 
            y = ordonnee(ev)
            # Calculer la distance entre le clic et le centre du cercle
            distance = ((x - x_cercle1)**2 + (y - y_cercle)**2)**0.5
            distance2 = ((x - x_cercle2)**2 + (y - y_cercle)**2)**0.5
            # Vérifier si la distance est inférieure ou égale au rayon du cercle
            if distance <= rayon_cercle:
                return "aleatoire"
            elif distance2<= rayon_cercle:
                return "manuel"

def regle():
    """ affiche une nouvelle fenetre pour affihcer les regles graphiquement
    params: aucun 
    --> return None """
    ferme_fenetre()
    cree_fenetre(800,800)
    regle_jeu = str(lire_fichier("regle.txt"))
    while True:
        # affiche la fenetre 
        retour_menu()
        rectangle(0,0,800,800,remplissage = "skyblue")
        texte(400,20,"REGLE DU JEU",ancrage = "center")
        rectangle(20,50,780,780,remplissage= "#0078B2")
        texte(55,55,f"{regle_jeu}",couleur = "#869593")
        mise_a_jour()

        ev = donne_ev()
        ty = type_ev(ev)
        if ty == "Quitte": 
            ferme_fenetre()
            exit(0)
        


    ferme_fenetre()

