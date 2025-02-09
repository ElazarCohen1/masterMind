from random import *

#grille


def cree_grille():  # elazar 
  """ crée une liste de liste avec que des None en 7*7 
  aucun parametre
  --> return grille (liste de liste)"""
  grille = []
  for ligne in range(7):
    grille.append(list([None] * 7))
  return grille

def affiche_plateau(grille, languettes_H, languettes_V):  # elazar vu
  """Affiche le plateau avec les billes et les languettes verticales et horizontales
  param : grille (matrice de None ou bille(str)) , languette_H (matrice de bool (True ou False)), languette_V (matrice True ou False) 
  --> return None"""
  supprime_bille(bille, grille, languettes_H, languettes_V)
  lst_V_temp = inverser_languette(languette_V)

  for ligne in range(len(grille)):
    for elm in range(len(grille[ligne])):

      # Affichage de la languette verticale
      if not lst_V_temp[ligne][elm]:
        print("v", end=" ")
      else:
        print(" ", end=" ")

      # Affichage de la languette horizontale
      if not languettes_H[ligne][elm]:
        print("h", end=" ")
      else:
        print(" ", end=" ")

      # Affichage de la case de la grille vide
      if grille[ligne][elm] is None:
        print(" - ", end=" | ")
      else:
        print(grille[ligne][elm], end=" | ")

    # Ligne vide pour séparer les lignes
    print("\n")


# languettes

def inverser_languette(lst_de_lst):  # elazar vu
  """ inverse la matrice  
  param: lst_de_lst (matrice)
  --> return lst_inversé
  >>> inverser_languette([[False,True,False], [False,True,True], [True,True,False]])
  [[False, False, True], [True, True, True], [False, True, False]]"""
  lst_temp = []
  for i in range(len(lst_de_lst)):
    temp = []
    for j in range(len(lst_de_lst[i])):
      temp.append(lst_de_lst[j][i])
    lst_temp.append(temp)
  return lst_temp

def decalage_gauche(lst):  #elazar
  """decale la liste vers la gauche
  param: lst 
  --> return nv_lst: la nouvelle liste decaler vers la gauche
    exemples : 
    >>> decalage_gauche([1 ,2, 3, 4, 5])
    [2, 3, 4, 5, 1]"""
  nv_lst = []
  for i in range(len(lst) - 1):
    nv_lst.append(lst[i + 1])
  nv_lst.append(lst[0])
  return nv_lst


def decalage_droite(lst):  #elazar vu
  """ decale la liste vers la droite 
  param: lst 
  --> return nv_lst: la nouvelle liste decaler vers la droite
    exemples : 
    >>> decalage_droite([1,2,3,4,5])
    [5, 1, 2, 3, 4]"""
  nv_lst = []
  nv_lst.append(lst[len(lst) - 1])
  for i in range(len(lst) - 1):
    nv_lst.append(lst[i])
  return nv_lst


def cree_languette():  #elazar
  """crée une languette vertical (liste) avec des Troue (True) ou pas (False)
    --> return languette (liste)
    >>> languette()
    [True, False, True, False, True, False, True]"""
  liste = [True, False, False
           ]  # prend de cette liste pour creer aleatoirement les languettes
  languette = []
  for i in range(7):
    languette.append(choice(liste))
  return languette

def languettes():  #elazar 
  """crée une matrice pour les languettes verticale et horizontale 
  --> return languette_H,languette_V (matrice de True ou False)"""
  languette_H = []
  languette_V = []
  for i in range(7):
    languette_temp_H = cree_languette()
    languette_temp_V = cree_languette()
    languette_H.append(languette_temp_H)
    languette_V.append(languette_temp_V)
  verifie_languette(languette_H)
  verifie_languette(languette_V)
  return languette_H, languette_V


def verifie_languette(languette):  #elazar
  """verifie si une languette n'a pas de trou du tout (il en faut min 3)
      verifie si il y'a pas trop de True (>4/7) 
      param : langette (matrice de True ou False)
      --> return None
      >>> verifie_languette([False, False, False, False, False, False, False ])
      [False, False, False, True, False, False, False ]
   """
  for _ in range(10):
    for ligne in languette:
      if ligne.count(True) >= 4:
        lst_temp = []

        for j, elm in enumerate(ligne):
          if elm == True:
            lst_temp.append(j)

        for i in range(3):
          lst_temp.pop()

        for k in lst_temp:
          ligne[k] = False

      for i in range(len(ligne)):
        if 1 <= i <= 5:

          if i == 1 and ligne[
              i - 1] == False and ligne[i] == False and ligne[6] == False:
            ligne[i - 1] = True
          elif i == 5 and ligne[
              i + 1] == False and ligne[i] == False and ligne[6] == False:
            ligne[i + 1] = True
          elif ligne[i -
                     1] == False and ligne[i] == False and ligne[i +
                                                                 1] == False:
            ligne[i] = True


def tirer_languette(languette_H, languette_V): #elazar
  """ demande si on veut tirer ou pousser une languette V ou H et deplace la liste de la languette (elle est circulaire)
      num grille de 1 a 7 de gauche a droite
      et de bas en haut
      exemple : 
      languette_H = [True,False,False]
      >>> tirer_languette(languette_H)
      >>> languette_H
      [False,True,False]"""
  orientation = input("quelles languettes veux tu decaler ? (V/H)")
  numero = int(input("le numero de la languette que tu veux decaler :  "))
  if orientation == "V":
    action = input("veux tu la monter (M) ou la baisser  (B) ? ")
    la = languette_V[numero - 1]  #numero de la languette
    if action == "M":  #on veut pousser
      temp = decalage_gauche(la)
      languette_V[numero - 1] = temp
    if action == "B":
      temp = decalage_droite(la)
      languette_V[numero - 1] = temp
  if orientation == "H":
    action = input("veux tu la pousser (P) ou la tirer (T) ? ")
    la = languette_H[numero - 1]
    if action == "P":  #on veut pousser
      temp = decalage_gauche(la)
      languette_H[numero - 1] = temp
    if action == "T":  # on veut tirer
      temp = decalage_droite(la)
      languette_H[numero - 1] = temp


# billes
def cree_bille(grille, languette_H, languette_V):  #maxence 
  """ on prend une coordonnée aleatoire et on affiche la bille sur le plateau 
  liste de couple random de 5 couple (bille)
  - verifier que bille pas sur la meme bille
  - verifier que bille pas dans un trou
  --> return bille (list(tuple))
  """
  bille = []
  while len(bille) < 5:  # bille aleatoire dans la grille
    x_bille = randint(0, 6)
    y_bille = randint(0, 6)
    #verifie que la bille n'est pas dans un troue
    if (x_bille, y_bille) not in bille and (languette_H[x_bille][y_bille] == False or languette_V[y_bille][x_bille]== False) and grille[x_bille][y_bille] == None:
      bille.append((x_bille, y_bille))
      grille[x_bille][y_bille] = " o "
  return bille


def supprime_bille(bille, grille, languette_H, languette_V):  #maxence 
  """si la bille est sur un troue on supprime la bille de la grille
  param: bille (list(tuple)), grille (matrice de None ou bille(str)), languette_H (matrice de True ou False), languette_V (matrice de True ou False))
  --> return None """
  for couple in bille:
    x, y = couple
    #on parcours les languttes et on regarde si il y'a un troue complet
    for i in range(7):
      for j in range(7):
        if (languette_H[i][j] == True) and (languette_V[j][i]== True) and (i, j) == (x, y):
          grille[i][j] = None
          bille.remove((x, y))


def gagne(bille, nb_coup):  # les deux
  """ si il n'y a plus de billes sur le plateau on a gagné
  params: bille (list(tuple)), nb_coup (int)
  --> return True or False, nb_coup (int)"""
  nb_coup += 1
  if len(bille) == 0:
    print("\n", "gagné! tu as fait tomber toute les billes en ", nb_coup," coups", "\n")
    return True, nb_coup
  else:
    return False, nb_coup


if __name__ == "__main__":
  import doctest
  languette_V, languette_H = languettes()
  grille = cree_grille()
  bille = cree_bille(grille, languette_H, languette_V)
  nb_coup = 0
  fin = False
  doctest.testmod()

  while not fin:
    affiche_plateau(grille, languette_H, languette_V)
    fin, nb_coup = gagne(bille, nb_coup)
    if fin == True:
      fin = not fin
      break
    tirer_languette(languette_H, languette_V)
