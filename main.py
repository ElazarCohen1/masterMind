from fltk import * 
from V1 import * 
from V2 import * 
from menu import *  
from info_partie_ia import * 



taille_fenetre,taille_case,lst_decalage ,languette_H, languette_V,lst_bille_supr,grille,nb_j_ordi,continuer,nb_j ,nb_coup,nb_joueur_coup,posit_languette_H, posit_languette_V = def_var()
cree_fenetre(taille_fenetre, taille_fenetre)
#initialiser variable 
menu_principal()
# main mis dans une fonction pour le reutiliser des que l'on rejoue 
main(taille_fenetre,taille_case,lst_decalage ,languette_H, languette_V,lst_bille_supr,grille,nb_j_ordi,continuer,nb_j ,nb_coup,nb_joueur_coup,posit_languette_H, posit_languette_V)



