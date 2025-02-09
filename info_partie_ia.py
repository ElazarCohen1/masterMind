#fichier fait par Maxence 
from fltk import * 
from V1 import * 
from menu import * 

def info_partie(grille,decalage,lst_bille_supr,lst_decalage,taille_fenetre,taille_case):
    """affiche les information de la partie tel que la languette bouger et les cordonnées des bille suprimmer
    params :
    grille : matrice de taille n x n (n = nombre de ligne) contenant les billes (None, "1", "2", "3", "4")
  languette_H : matrice de True et False corespondent au langaugettes horizontal
  languette_V : matrice de True et False corespondent au langaugettes vertical
  taille_fenetre : taille de la fenetre
  lst_bille_supr(lst):la liste des billes supprimé 
  lst_decalage: (matrice de 3) qui donne toute les info sur les decalge des languettes """
    
    if decalage != None:
        cote_decalage,languette_decaler = decalage

        if cote_decalage != None:
            lst_decalage.append(decalage)

        if len(lst_decalage)>3:
            lst_decalage.pop(0)
        
        if lst_bille_supr != None:
            if len(lst_bille_supr)>4:
                while len(lst_bille_supr)>4:
                    lst_bille_supr.pop(0)

        lst_affichage = []
        lst_affichage.append(lst_decalage)
        lst_affichage.append(lst_bille_supr)
        
        affichage_info_partie(lst_affichage,taille_fenetre,taille_case,grille)
        

def affichage_info_partie(lst_affichage,taille_fenetre,taille_case,grille):
    """affiche les info sur les langete et sur les bille suprimer
    params:
    lst_affichage,taille_fenetre,taille_case,grille"""
    affichage_info_deplacement_languette(lst_affichage,taille_fenetre,taille_case)
    affichage_info_supr_bille(lst_affichage,taille_fenetre,taille_case,grille)

        


def affichage_info_deplacement_languette(lst_affichage,taille_fenetre,taille_case):
    """affiche les 3 derniere languette qui ont ete deplacer
    params :  lst_affichage (matrice triple qui prend les informations comme le decalage des languettes)
                taille_fenetre
                taille_case: la taille d'une case (50)
    --> return None"""
    x_info,y_info = taille_fenetre*7.3/10 ,taille_fenetre/40
    a= 0
    num_V = ["a", "b", "c", "d", "e", "f", "g"]
    efface("qq")
    
    if lst_affichage[0]!=None and a < len(lst_affichage[0]):
        rectangle(x_info-10,y_info,x_info+200,y_info+taille_case*len(lst_affichage[0]),remplissage = 'white',tag='est')
        for _ in range(len(lst_affichage[0])):
            if lst_affichage[0][a][1] != None and (lst_affichage[0][a][0] == "Droite" or lst_affichage[0][a][0]== "Gauche"):
                tmp_4 = lst_affichage[0][a][1]
                tmp_4 = num_V[tmp_4]
            else:
                tmp_4 = lst_affichage[0][a][1]+1
            if lst_affichage[0][a][0] == "Droite" or lst_affichage[0][a][0]== "Gauche":
                texte(x_info,y_info,f"la languette {tmp_4} a \nete decaler a {lst_affichage[0][a][0]}",taille= 15,tag="qq")
            else :
                texte(x_info,y_info,f"la languette {tmp_4} a \nete decaler en {lst_affichage[0][a][0]}",taille= 15,tag="qq")
            mise_a_jour()
            y_info+= taille_case
            a+=1
        
            

def affichage_info_supr_bille(lst_affichage,taille_fenetre,taille_case,grille):
    """affiche les 4 derniere bille qui on ete suprimmer ainsi que les cordoné de la ou elle etait
    params :  lst_affichage (matrice triple qui prend les informations comme le decalage des languettes)
                taille_fenetre
                taille_case: la taille d'une case (50)
                grille : matrice contenant les bille
    --> return None
    """

    x_info_2,y_info_2 = taille_fenetre/10 ,taille_fenetre*3/4
    b = 0

    num_V = ["a", "b", "c", "d", "e", "f", "g"]
    couleur_bille = ["red","black","yellow","green","grey"]
    
    if lst_affichage[1]!=None and b < len(lst_affichage[1]):
        rectangle(x_info_2-50,y_info_2-25,x_info_2+50,y_info_2+taille_case*len(lst_affichage[1])-25,remplissage = 'white')
        efface("fh")
        for i in range(len(lst_affichage[1])):
            if lst_affichage[1][i]!=None:
                j,k,bille_supr = lst_affichage[1][i]
                if bille_supr ==" o ":
                    couleur_b = couleur_bille[0]
                else:
                    bille_supr = int(bille_supr)
                    couleur_b = couleur_bille[bille_supr]
                tmp = num_V[j]
                if grille[j][k] == None:
                    
                    cercle(x_info_2*3/4,y_info_2,x_info_2/4,couleur_b,couleur_b,tag="fh")
                    texte(x_info_2+10,y_info_2- 10,f"{tmp} {k+1}",taille=15,tag="fh")
                    y_info_2+= taille_case
                    mise_a_jour()
            b+=1
            


def affichage_joueur_coup(taille_fenetre,nb_joueur_coup ,ev_tirer_languette,decalage_languette,j_jouant):
    """affiche a quel joueur c'est a jouer
    params :  taille_fenetre
                nb_joueur_coup : int permetant de savoir a qui c'est de jouer
                ev_tirer_languette : evenment du decalage de langette
                decalage_languette : info sur langette decaler
                j_jouant : list trie contenent les joueru qui joue encore
    --> return nb_joueur_coup
    """
    x_afi,y_afi = taille_fenetre/2, taille_fenetre*18.5/20

    i,j = decalage_languette
    if ev_tirer_languette !=  None and i!= None and j != 15 :
        nb_joueur_coup += 1
    if nb_joueur_coup > len(j_jouant)-1:
        nb_joueur_coup=0

    if nb_joueur_coup != None:
        efface("xx")
        texte(x_afi,y_afi,f"c'est au joueur \n{j_jouant[nb_joueur_coup]} de jouer",ancrage= "center",taille=30,tag="xx")
        mise_a_jour()
        
    
    return nb_joueur_coup



def ia_random_respectueuse(languette_H,languette_V,posit_languette_H,posit_languette_V,x,y,nb_j_ordi,ev_languette,nb_joueur_coup,j_jouant):
    """un ia random qui joue avec vous apres les tour de tout le monde"""
    decalage=None
    if x == 0 and y == 0 and nb_j_ordi == len(j_jouant)-1:
        nb_j_ordi = 0
        decalage = ia_random_irrespectueuse(languette_H,languette_V,posit_languette_H,posit_languette_V)
    #condition a ameliorer pour voir uniquement quand c'est avec des coup de languette fonctionel
    if ev_languette!= None :
        nb_j_ordi += 1
        nb_joueur_coup +1
    if decalage == None:
        decalage = (None,15)
    return nb_j_ordi,decalage,nb_joueur_coup
    

def ia_random_irrespectueuse(languette_H,languette_V,posit_languette_H,posit_languette_V):
    """une fausse ia qui joue en solo de facon random sans but precis, elle va vivre sa vie 
    et faire une partie avec elle meme en gros jusqu'a ce que tout les bille soivent suprimmerou que il y a un gagnant"""
    decalage = None
    while decalage == None:
        V_ou_H = randint(0,1)
        D_ou_G = randint(0,1)
        ia_languette = randint(0,6)
        if V_ou_H == 0 and D_ou_G == 0 and posit_languette_H[ia_languette] in (1, 2):
            languette_H[ia_languette] = decalage_droite(languette_H[ia_languette])
            posit_languette_H[ia_languette] += 1
            decalage = ("Droite",ia_languette)
        elif V_ou_H == 0 and D_ou_G == 1 and posit_languette_H[ia_languette] in (2, 3):
            languette_H[ia_languette] = decalage_gauche(languette_H[ia_languette])
            posit_languette_H[ia_languette] -= 1
            decalage = ("Gauche",ia_languette)

        elif V_ou_H == 1 and D_ou_G == 0 and posit_languette_V[ia_languette] in (2, 3):
            languette_V[ia_languette] = decalage_droite(languette_V[ia_languette])
            posit_languette_V[ia_languette] -= 1
            decalage = ("Bas",ia_languette)
            
        elif V_ou_H == 1 and D_ou_G == 1 and posit_languette_V[ia_languette] in (1, 2):
            languette_V[ia_languette] = decalage_gauche(languette_V[ia_languette])
            posit_languette_V[ia_languette] += 1
            decalage = ("Haut",ia_languette)
        
        if decalage != None:
            return decalage

