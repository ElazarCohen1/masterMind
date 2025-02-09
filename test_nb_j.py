from random import *
from fltk import *
from V1 import *
from V2 import *
from menu import *

def placer_bille(grille,nb_j,languette_H,languette_V,posit_langette_H,posit_langette_V, taille_fenetre,lst_bille_supr): 
    """--> return le nb de joueur qui joue
    - x a toi de placer ta num bille 
    - y a toi 
    - etc 
    - evenement
    - pour placer la bille on recupere les coordonnées de la souris et si il est dans le plateau tk on peut ajouter la bille a la grille"""
    joueur = 0
    bille = 0
    #parcourir la grille
    for ligne in range(len(grille)):
        for j in range(len(ligne)):
          efface("j")
          texte(taille_fenetre / 2 - 200,20,f" a toi de poser ta bille joueur : {joueur+1}",tag="j")
          mise_a_jour()
          affiche_plateau_tk(grille, languette_H, languette_V, posit_langette_H,posit_langette_V, taille_fenetre,lst_bille_supr)
          ev = donne_ev()
          ty = type_ev(ev)
          x = abscisse(ev)
          y == ordonnee(ev)
          if ty == "Quitte":
             ferme_fenetre()
             exit(0)
          elif ty == "ClicGauche":
            # si il y'a pas de troue et si il y'a pas deja de bille et si  l'on place sur le plateau 
            if (languette_H[ligne][j] and languette_V[ligne][j]) == False and grille[ligne][j] == None and 225<x<575 and 225<y<575:
              grille[ligne][j] = str(joueur+1) 
              bille+=1
              joueur +=1
          if joueur == nb_j:
            joueur = 0
          if bille == int(5*nb_j): 
            return
            