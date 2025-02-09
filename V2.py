from random import *
from fltk import *
from info_partie_ia import * 
from V1 import *

# plateau tk 

def affiche_plateau_tk(grille, languette_H, languette_V, posit_languette_H, posit_languette_V, taille_fenetre,lst_bille_supr,nb_j):  #elazar/ maxence (60/40)
  """  prend le plateau et les languettes et les billes et les affiches dans fltk 

  params : 
    grille : matrice conenant les billes, des None si rien sinon 1,2,3,4 en fonction du joueur et o pour bille ordi
    languette_H :(matrice de True False) ( affichage de couleur orange)
    languette_V: (matrice de True False) ( affiche de couleur blanc)
    posit_languette_H : liste des position de chaque languette horizontal
    posit_languette_V : liste des position de chaque languette vertical
    taille_fenetre : taille de la fenetre (en pixel)
    lst_bille_supr : la liste des billes plus sur le plateau
    nb_j(int) : le nombre de joueur 
    
    return rien, ne fait que de l'affichage"""
  
  affichage_pos_languette(posit_languette_H, posit_languette_V, taille_fenetre)
  affiche_mun_languette(taille_fenetre)
  affichage_bille_a_joueur(nb_j,taille_fenetre)
  
  lst_bille_supr = supprime_bille_tk(grille, languette_H, languette_V,lst_bille_supr)
  l_V_inversé = inverser_languette(languette_V)
  taille_case = 50
  y = taille_fenetre / 2 - (taille_case * 3.5)
  for ligne in range(len(grille)):
    x = taille_fenetre / 2 - (taille_case * 3.5)
    for j in range(len(grille[ligne])):
      if l_V_inversé[ligne][j] and languette_H[ligne][j] == True:  # si les deux ont des Troues
        rectangle(x, y, x + taille_case, y + taille_case,remplissage="black")

      elif languette_H[ligne][j] == False:  #si la languette horizontal est rempli
        rectangle(x, y, x + taille_case, y + taille_case, remplissage="orange")

      elif l_V_inversé[ligne][j] == False:  # si la languette vertical est rempli
        rectangle(x, y, x + taille_case, y + taille_case, remplissage="white")
      if l_V_inversé[ligne][j] == False and languette_H[ligne][j] == False:
        rectangle(x, y, x + taille_case, y + taille_case, remplissage="purple")
      #affichage des billes
      if grille[ligne][j] == "1":
        cercle(x + taille_case / 2,y + taille_case / 2,taille_case / 3,remplissage="black")
      elif grille[ligne][j] == "2":
        cercle(x + taille_case / 2, y + taille_case / 2,taille_case / 3,remplissage="yellow")
      elif grille[ligne][j] == "3":
        cercle(x + taille_case / 2, y + taille_case / 2,taille_case / 3,remplissage="green")
      elif grille[ligne][j] == "4":
        cercle(x + taille_case / 2,y + taille_case / 2,taille_case / 3,remplissage="gray")
      elif grille[ligne][j] == " o ":
        cercle(x + taille_case / 2, y + taille_case / 2,taille_case / 3,remplissage="red")
      x += taille_case
    y += taille_case
  mise_a_jour()
  return lst_bille_supr

def occurence_joueur(grille):  #elazar
  """crée un dictionnaire avec les noms des joueurs(int) comme clé et compte les occurences des billes
  param : grille (matrice de None ou chiffre (bille))
  --> return le dico"""

  dico = {}
  for i in grille:
    for j in i:
      if j != None:
        num = j
        dico[f"{num}"] = dico.get(num, 0) + 1
  return dico

# bille tk

def bille_aleatoire(grille,nb_j,languette_H,languette_V,posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,ia_yes_or_no): 
  """ajoute les billes aleatoirement sur la fenetre 
  params :
  grille (matrice) 
  nb_j (int): le nombre de joueur recupere du fichier secondaire
  languette_H :(matrice de True False) ( affichage de couleur orange)
  languette_V: (matrice de True False) ( affiche de couleur blanc)
  posit_languette_H : liste des position de chaque languette horizontal
  posit_languette_V : liste des position de chaque languette vertical
  taille_fenetre : taille de la fenetre (en pixel)
  lst_bille_supr : la liste des billes plus sur le plateau
  --> return la liste des coordonnées des billes sur le plateau (liste de tuple) 
  """
  bille = []
  joueur = 0
  ia_yes_or_no = lire_fichier("IA.txt")
  while len(bille) < 5*nb_j:
    ev = donne_ev()
    ty = type_ev(ev)
    if ty =="Quitte":
      ferme_fenetre()
      exit(0)
    rectangle(190,10,600,100)
    texte(400,55,"posage des billes en cours ...",ancrage = "center")

    affiche_plateau_tk(grille, languette_H, languette_V, posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,nb_j)
    # cree bille aleatoire
    x_bille = randint(0,6)
    y_bille = randint(0,6)
    #condition pour ajouter une bille (si elle est pas sur un troue etc )
    if (x_bille, y_bille) not in bille and (languette_H[x_bille][y_bille] == False or languette_V[y_bille][x_bille]== False) and grille[x_bille][y_bille] == None:
      bille.append((x_bille,y_bille))
      grille[x_bille][y_bille ] = str(joueur+1)
      if len(bille) %5 == 0: 
        joueur +=1
  if ia_yes_or_no == "ON":
    cree_bille(grille,languette_H,languette_V)
  return bille

def placer_bille(grille,nb_j,languette_H,languette_V,posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,ia_yes_or_no): #elazar/maxence
  """--> return le nb de joueur qui joue
  params: 
  les meme que affiche plateau tk / bille aleatoire 

  - pour placer la bille on recupere les coordonnées de la souris et si il est dans le plateau tk on peut ajouter la bille a la grille"""
  taille_case = 50
  joueur = 0
  bille = 0
  ia_yes_or_no = lire_fichier("IA.txt")
  #tant que il y'a pas 5 billes par joueur 
  while bille < 5*nb_j :          
    efface("j")
    rectangle(0, 0, taille_fenetre, taille_fenetre, remplissage="skyblue")
    texte(taille_fenetre / 2 - 200,20,f" a toi de poser ta bille joueur : {joueur+1}",tag="j")
    affiche_plateau_tk(grille, languette_H, languette_V, posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,nb_j)
    mise_a_jour()
    ev = donne_ev()
    ty = type_ev(ev)
    if ty == "Quitte":
        ferme_fenetre()
        exit(0)
    elif ty == "ClicGauche":
      x = abscisse(ev)
      y = ordonnee(ev)
      # calcule la case du plateau en fonction des coordonées 
      pos_h = int((y - 225) / taille_case)
      pos_v = int((x - 225) / taille_case)
      # si il y'a pas de troue et si il y'a pas deja de bille et si l'on se place bien  sur le plateau 
      #alors on ajoute la bille
      if 225<x<575 and 225<y<575 and (languette_H[pos_h][pos_v] == False or languette_V[pos_v][pos_h] == False) and grille[pos_h][pos_v] == None  :
        grille[pos_h][pos_v] = str(joueur+1) 
        bille+=1
        joueur +=1
      #pour boucler et faire les joueurs un part un
    if joueur == nb_j:
      joueur = 0
    retour_menu()

  if ia_yes_or_no == "ON":
    cree_bille(grille,languette_H,languette_V)
  efface("j")
      
def affichage_bille_a_joueur(nb_j, taille_fenetre):
  """affiche en fonction du nombre de joueur quel bille est a qui
  nb_j : nombre de joueur
  taille_fenetre : taille de la fenetre
  
  --> return None, affiche quel bille va quel joueur
  """
  couleur = ("black", "yellow", "green", "gray")
  taille_case = 50

  x = taille_fenetre / 2 - (taille_case * 3.5) + 98 / 10 * taille_case
  y = taille_fenetre / 2 - (taille_case * 3.5) + 75 / 10 * taille_case
  for i in range(1,nb_j+1):
    texte(x, y, f"la bille {couleur[i-1]} \n est au joueur {i}", couleur[i-1],"center", taille= 15)
    y += 50

def supprime_bille_tk(grille, languette_H, languette_V,lst_bille_supr):  #maxence
  """verifie si les cordonne de la languette verical et horizontal correspondante son True,
  et qu'il y a une bille a cette endroit. si c'est la cas alors on remplace la valeur de 
  cette bille dans la grille par None
  
  grille : matrice de taille n x n (n = nombre de ligne) contenant les billes (None, "1", "2", "3", "4")
  languette_H : matrice de Tue False (des languette horizontal)
  languette_V : matrice de Tue False (des languette vertical)

  return None, remplace la valeur de grille par non si celle des languette est True
  """
  
  for i in range(7):
    for j in range(7):
      if (languette_H[i][j] == True) and (languette_V[j][i]== True) and grille[i][j] != None:
        lst_bille_supr.append((i,j,grille[i][j]))
        grille[i][j] = None
  return lst_bille_supr

#  fin 

def gagne_tk(grille,dico_j, nb_j,ia_yes_or_no):  #maxence
  """ si il n'y a plus de billes sur le plateau on a gagné ou si il reste les billes d'un joueur
  
  grille : matrice de taille n x n (n = nombre de ligne) contenant les billes (None, "1", "2", "3", "4")
  dico_j : dictionnaire contenant les joueurs 
  nb_j : nombre de joueur
  --> return True si la longeueur de la liste de joueur est 1, False sinon False
  """
  lst,vide = gagnant(dico_j,ia_yes_or_no)
  # si il rester un seul joueur
  if len(lst) == 1 and nb_j > 1:
    return True 
  for i in range(len(grille)):
    for j in range(len(grille[i])): 
      if  grille[i][j] != None:
        return False
  return True
  
def gagnant(dico_j,ia_yes_or_no): #elazar/maxence   #60/40
  """recupere un dico de joueur avec le nombre de bille
  --> return la liste avec les joueur qui ont plus de 0 billes  
  
  dico_j : dictionnaire contenant les joueurs

  return j_encore_en_lisse (liste) qui renvoit les joueurs qui ont au moins une bille 
  """
  j_encore_en_lisse = []
  for cle, valeur in dico_j.items():
    if valeur > 0 and cle != " o ":
      j_encore_en_lisse.append(int(cle))
    elif cle == ' o ':
      j_encore_en_lisse.append("ordi")

  tmp = 0
  if "ordi" in j_encore_en_lisse:
    tmp=1
    j_encore_en_lisse.remove("ordi")
  
  #trie un liste dans l'ordre croissant uniquement des int
  lst_j = sorted(j_encore_en_lisse)
  if tmp == 1:
    lst_j.append("ordi")
    j_encore_en_lisse.append("ordi")

  return j_encore_en_lisse,lst_j

def afficher_perdant(dico_j, nb_j,j_jouant,ia_yes_or_no):  #elazar
  """affiche quand un joueur perd c'est a dire qu'il n'a plus de bille sur le plateau

  dico_j : dictionnaire contenant les joueurs
  nb_j : nombre de joueur

  return None, affiche le jouer qui perd
  """
  ia_yes_or_no = lire_fichier("IA.txt")
  y = 50
  efface("xxxx")
  for i in range(1,nb_j+1):
    if str(i) not in dico_j:
      texte(5, y, f" joueur {i} a perdu !!! ",tag='xxxx')
      y += 30
  if "ordi" not in j_jouant and ia_yes_or_no == "yes":
    texte(5, y, f" ordi a perdu !!! ",tag='xxxx')


# languettes 
      
def tirer_languette_tk(languette_H, languette_V, posit_languette_H,posit_languette_V,nb_coup):  #elazar/maxence  # 80/20
  """tire ou pousse une languette et change directement les languettes original
   
   languette_H : matrice True False des languettes horizontales
   languette_V : matrice True False des languettes verticales
   posit_languette_H : liste des position des languettes horizontales
   posit_languette_V : liste des position des languettes verticales
   nb_coup : le nb_coup precedecent 

   return x,y : coordonnée de la souris cliquée
          decalage : tuple (sens de la languette,case du plateau ou ca a decaler )
          ev : l'evenement fait 
          nb_coup(int): le nombre de tirrette tirer pour un seule joueur  
   """
  taille_case = 50
  ev = donne_ev()
  ty = type_ev(ev)
  x, y = 0, 0
  decalage = (None,15)
  if ty == "Quitte":
    ferme_fenetre()
    exit(0)
  elif ty == "ClicGauche":
    x = abscisse(ev)
    y = ordonnee(ev)
    # calcule la case du plateau avec les coordonnées 
    pos_h = int((y - 225) / taille_case)
    pos_v = int((x - 225) / taille_case)
    # si on decale les languettes horizontals vers la droite
    if x < 225 and 225 < y < 575 and posit_languette_H[pos_h] in (1, 2):
      la = int((y - 225) / taille_case)
      l1 = languette_H[la]
      languette_H[la] = decalage_droite(l1)
      posit_languette_H[la] += 1
      decalage = ("Droite",la)
      nb_coup+=1
    # si on decale les languettes horizontals vers la gauche
    elif x > 575 and 225 < y < 575 and posit_languette_H[pos_h] in (2, 3):
      la = int((y - 225) / taille_case) 
      l1 = languette_H[la]
      languette_H[la] = decalage_gauche(l1)
      posit_languette_H[la] -= 1
      decalage = ("Gauche",la)
      nb_coup+=1
    # si on decale les languettes vertical vers la droite
    elif y < 225 and 225 < x < 575 and posit_languette_V[pos_v] in (2, 3):
      la_2 = int((x - 225) / taille_case)
      l2 = languette_V[la_2]
      languette_V[la_2] = decalage_droite(l2)
      posit_languette_V[la_2] -= 1
      decalage = ("Bas",la_2)
      nb_coup+=1
    # si on decale les languettes vertical vers la gauche
    elif y > 575 and 225 < x < 575 and posit_languette_V[pos_v] in (1, 2):
      la_2 = int((x - 225) / taille_case)
      l2 = languette_V[la_2]
      languette_V[la_2] = decalage_gauche(l2)
      posit_languette_V[la_2] += 1
      decalage = ("Haut",la_2)
      nb_coup+=1

  return x, y, decalage , ev,nb_coup

def initialisation_languettes(): #maxence
  """initialise la position de tout les languette de base a 2 soit position du milieux
  return posit_languette_H, posit_languette_V : liste des position des languettes
  """
  posit_languette_V, posit_languette_H = [], []
  for ligne in range(7):
    posit_languette_V.append(2)
    posit_languette_H.append(2)
  return posit_languette_H, posit_languette_V


def affiche_mun_languette(taille_fenetre):  #maxence
  """affiche les mumero des languettes veritical(1,2,3,4,5,6,7) et des horizontal (a,b,c,d,e,f,g)
  param:
  taille_fenetre : taille de la fenetre
  
  return None, affihe les numero des languette vertical et horizontal
  """
  taille_case = 50
  y_vertical = taille_fenetre / 2 - (taille_case * 3.5) + 1 / 2 * taille_case
  x_droite = taille_fenetre / 2 - (taille_case * 3.5) - 1 / 2 * taille_case
  x_gauche = taille_fenetre / 2 - (taille_case *3.5) - 1 / 2 * taille_case + 8 * taille_case
  num_V = ["a", "b", "c", "d", "e", "f", "g"]
  num_H = [1, 2, 3, 4, 5, 6, 7]
  y_haut = taille_fenetre / 2 - (taille_case * 3.5) - 1 / 4 * taille_case
  y_bas = taille_fenetre / 2 - (taille_case *3.5) - 1 / 2 * taille_case + 8 * taille_case
  x_horizontal = taille_fenetre / 2 - (taille_case * 3.5) + 1 / 2 * taille_case
  for elem in num_V:
    texte(x_droite, y_vertical, elem, "black", "center", taille=30)
    texte(x_gauche, y_vertical, elem, "black", "center", taille=30)
    y_vertical += taille_case
  for elem in num_H:
    texte(x_horizontal, y_haut, elem, "black", "center", taille=30)
    texte(x_horizontal, y_bas, elem, "black", "center", taille=30)
    x_horizontal += taille_case

def choix_pos_languettes(grille, languette_H, languette_V, posit_languette_H,
                        posit_languette_V, taille_fenetre,lst_bille_supr,nb_j,lst_decalage):  #maxence
  """permet de choisir dans quel position le joueur initialiser ses languette en debut de partie

  grille : matrice de taille n x n (n = nombre de ligne) contenant les billes (None, "1", "2", "3", "4")
  languette_H : matrice de True et False corespondent au langaugettes horizontal
  languette_V : matrice de True et False corespondent au langaugettes vertical
  posit_languette_H : liste des position des languettes horizontal
  posit_languette_V : liste des position des languettes vertical
  taille_fenetre : taille de la fenetre
  lst_bille_supr(lst):la liste des billes supprimé 
  nb_j(int):nombre de joueur 
    lst_decalage: (matrice de 3) qui donne toute les info sur les decalge des languettes 
  
  return None,par effet de boor modifier la psotion des languette verticle et horizontal en fonction des choix du joueur
  """
  rectangle(0, 0, taille_fenetre, taille_fenetre, remplissage="skyblue")
  depart = False
  while not depart:

    rectangle(0, 0, taille_fenetre, taille_fenetre, remplissage="skyblue")
    affiche_plateau_tk(grille, languette_H, languette_V, posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,nb_j)
    x, y, decalage, ev,nb_coup = tirer_languette_tk(languette_H, languette_V, posit_languette_H,posit_languette_V,0)
    taille_case = 50
    x_rectangle, y_rectangle = (taille_fenetre / 12 -taille_case), (taille_fenetre / 10) * 8.5
    x_fin_rectangle, y_fin_rextangle = x_rectangle + taille_case * 3, y_rectangle + taille_case * 1.5
    rectangle(x_rectangle,y_rectangle,x_fin_rectangle,y_fin_rextangle,remplissage="red",tag="tt")
    x_texte, y_texte = taille_case * 1.75, y_rectangle + 3 / 4 * taille_case
    texte(x_texte,y_texte,f"fin \nde l'initialisation \ndes languettes","black","center","Helvetica",15,tag="tt")
    info_partie(grille,decalage,lst_bille_supr,lst_decalage,taille_fenetre,taille_case)
    retour_menu()
    if x_rectangle < x < x_fin_rectangle and y_rectangle < y < y_fin_rextangle:
      efface("tt")
      efface("qq")
      efface("est")
      depart = not depart

def affichage_pos_languette(posit_languette_H, posit_languette_V,taille_fenetre):  #maxence 
  """affiche la position des languette sur les cote du plateau de jeu
  posit_languette_H : liste des position des languettes horizontales
  posit_languette_V : liste des position des languettes verticales
  taille_fenetre : taille de la fenetre

  return None, affiche les position des languettes vertical et horizonatal
  """
  taille_case = 50
  efface("k")
  taille_case_2 = taille_case * 4 / 5
  taille_decalage = taille_case_2 / 2
  y_horizontal = taille_fenetre / 2 - (taille_case * 3.5) + taille_decalage / 4
  x_vertical = taille_fenetre / 2 - (taille_case * 3.5) + taille_decalage / 4

  for i in range(7):
    #affichage languette horizontal à droite

    x_droite, x_gauche = taille_fenetre / 2 - (taille_case *3.5) + taille_case * 7, taille_fenetre / 2 - (taille_case * 3.5)

    for _ in range(posit_languette_H[i]):
      rectangle(x_droite,y_horizontal,x_droite + taille_case_2 / 2 + taille_decalage,y_horizontal + taille_case_2,remplissage="orange",tag="k")
      x_droite += taille_case_2

    #affichage languette coté gauche
    if posit_languette_H[i] == 1:
      tmp = 3

    elif posit_languette_H[i] == 2:
      tmp = 2

    elif posit_languette_H[i] == 3:
      tmp = 1

    for _ in range(tmp):
      rectangle(x_gauche - taille_case_2 / 2 - taille_decalage,y_horizontal,x_gauche,y_horizontal + taille_case_2, remplissage="orange",tag="k")
      x_gauche -= taille_case_2
    #affichage languette bas
    y_bas = taille_fenetre / 2 - (taille_case *3.5) + taille_case * 8 - taille_decalage / 2
    if posit_languette_V[i] == 1:
      tmp_2 = 3

    elif posit_languette_V[i] == 2:
      tmp_2 = 2

    elif posit_languette_V[i] == 3:
      tmp_2 = 1

    for _ in range(tmp_2):
      rectangle(x_vertical,y_bas,x_vertical + taille_case_2,y_bas - taille_case_2,remplissage="white",tag="k")
      y_bas += taille_case_2

    #affiche languette haut
    y_haut = taille_fenetre / 2 - (taille_case * 3.5)

    for _ in range(posit_languette_V[i]):
      rectangle(x_vertical,y_haut,x_vertical + taille_case_2,y_haut - taille_case_2,remplissage="white",tag="k")
      y_haut -= taille_case_2
    x_vertical += taille_case
    y_horizontal += taille_case

#chose technique 

def def_var(): #elazar
    """initialise toute les variables necessaires pour recommencer une partie 
    param:aucun 
    --> return toute les variables initialiser """
    taille_fenetre = 800
    taille_case = 50
    lst_decalage = []
    languette_H, languette_V = languettes()
    lst_bille_supr = []
    grille = cree_grille()
    nb_j_ordi = 0
    continuer = True
    nb_j = int(lire_fichier("nb_joueur.txt"))
    nb_coup = 0
    nb_joueur_coup = 0
    posit_languette_H, posit_languette_V = initialisation_languettes()
    return taille_fenetre,taille_case,lst_decalage ,languette_H, languette_V,lst_bille_supr,grille,nb_j_ordi,continuer,nb_j ,nb_coup,nb_joueur_coup,posit_languette_H, posit_languette_V

def choisir_f_billes(grille,nb_j,languette_H,languette_V,posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,ia_yes_or_no): 
  """en fonction du choix du joueur appelle la fonction de pose aleatoire ou placer bile manuel
  params: les meme que affiche plateau_tk etc 
  --> return None """
  ia_yes_or_no = lire_fichier("IA.py")
  choix_bille = lire_fichier("menu_bille.txt")
  if choix_bille == "manuel":
    placer_bille(grille,nb_j,languette_H,languette_V,posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,ia_yes_or_no)
  elif choix_bille == "aleatoire": 
    bille_aleatoire(grille,nb_j,languette_H,languette_V,posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,ia_yes_or_no)

def main(taille_fenetre,taille_case,lst_decalage ,languette_H, languette_V,lst_bille_supr,grille,nb_j_ordi,continuer,nb_j ,nb_coup,nb_joueur_coup,posit_languette_H, posit_languette_V): 
  """fais une partie en entier (mise en fonction pour rejouer depuis le menu)
  params : toute les variables initialiser dans def_var 
  --> return None """
  rectangle(0, 0, taille_fenetre, taille_fenetre, remplissage="skyblue")
  choix_pos_languettes(grille, languette_H, languette_V, posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,nb_j,lst_decalage)
  ia_yes_or_no = lire_fichier("IA.txt")
  choisir_f_billes(grille,nb_j,languette_H,languette_V,posit_languette_H,posit_languette_V, taille_fenetre,lst_bille_supr,ia_yes_or_no)
  rectangle(0, 0, taille_fenetre, taille_fenetre, remplissage="skyblue")
  nb_coup = 0
  nb_j_ordi = 0
  #decalage_languette = (None,15)
  while continuer:
    
    ev = donne_ev()
    ty = type_ev(ev)
    #variable qui se reinitialise ou verifie a chaque tour
    dico_j = occurence_joueur(grille)
    j_gagnant,j_jouant = gagnant(dico_j,ia_yes_or_no)
    fin = gagne_tk(grille,dico_j,nb_j,ia_yes_or_no)
    rectangle(0, 0, taille_fenetre, taille_fenetre, remplissage="skyblue")
    afficher_perdant(dico_j,nb_j,j_jouant,ia_yes_or_no)
    # si on a pas perdu 
    if fin == False:
      lst_bille_supr = affiche_plateau_tk(grille, languette_H, languette_V,posit_languette_H,posit_languette_V,taille_fenetre,lst_bille_supr,nb_j)
      x,y, decalage_languette ,ev_languette,nb_coup= tirer_languette_tk(languette_H, languette_V, posit_languette_H,posit_languette_V,nb_coup)
      nb_joueur_coup = affichage_joueur_coup(taille_fenetre,nb_joueur_coup ,ev_languette,decalage_languette,j_jouant)
      info_partie(grille,decalage_languette,lst_bille_supr,lst_decalage,taille_fenetre,taille_case)

      #pour jeu avec joueur avec ordi
      if ia_yes_or_no == "ON" and "ordi" in j_jouant:  
        nb_j_ordi,decalage,nb_joueur_coup =ia_random_respectueuse(languette_H,languette_V,posit_languette_H,posit_languette_V,x,y,nb_j_ordi,ev_languette,nb_joueur_coup,j_jouant)
        nb_joueur_coup = affichage_joueur_coup(taille_fenetre,nb_joueur_coup ,1,decalage,j_jouant)
        i,j=decalage
        if i!= None and j!= 15:
          info_partie(grille,decalage,lst_bille_supr,lst_decalage,taille_fenetre,taille_case)
      
    # sinon si on a perdu 
    if fin is True:
      if ty == "Quitte":
          ferme_fenetre()
          exit(0)

      #efface tout et reaffiche une fenetre
      efface_tout()
      rectangle(0, 0, taille_fenetre, taille_fenetre, remplissage="skyblue")
      afficher_perdant(dico_j,nb_j,j_jouant,ia_yes_or_no)
      # si on a qu'un joueur on doit faire tomber les billes le plus vite possible
      if nb_j == 1:
          rectangle(0, 0, taille_fenetre, taille_fenetre, remplissage="skyblue")
          texte(800/2, 800/2, f"gagné\ntu as fait tomber toute les billes en {nb_coup} coups ",ancrage= "center",taille = 20)
          retour_menu()
      #sinon on affiche les joueurs qui ont perdu et le gagnant 
      elif len(j_gagnant) == 1 and nb_j > 1:
          texte(taille_fenetre/2 - 100, taille_fenetre/2-100, f"{str(j_gagnant)} a gagné", taille = 50)
          retour_menu()
    retour_menu() 
    mise_a_jour()

  ferme_fenetre()