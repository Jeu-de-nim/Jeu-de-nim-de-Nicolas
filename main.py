import random

def player_one_turn(N, j1):
  print("c'est à",j1,"de jouer")
  nb_allumettes_joueur = -1
  while(not nb_allumettes_joueur in range(1,4)):
    nb_allumettes_joueur = int(input("Combien d'allumettes souhaitez vous retirer ? (entre 1 et 3) : "))
  N = N - nb_allumettes_joueur
  if(N <= 0):
    print(j1,"Vous avez perdu !")
    return 0
  elif(N == 1):
    print(j1,"Vous avez gagné !")
    return 1
  else:
    return N


def player_two_turn(N,j2):
  print("c'est à",j2,"de jouer")
  nb_allumettes_joueur = -1
  while(not nb_allumettes_joueur in range(1,4)):
    nb_allumettes_joueur = int(input("Combien d'allumettes souhaitez vous retirer ? (entre 1 et 3) : "))
    N = N - nb_allumettes_joueur
    if(N <= 0):
      print(j2,"Vous avez perdu !")
      return 0
    elif(N == 1):
      print(j2,"Vous avez gagné !")
      return 1
    else:
      return N

def ordinateur_turn(N):
  print("Tour de l'ordinateur")
  nb_allumettes_ordinateur = 0
  if(N <= 4):
    nb_allumettes_ordinateur = N - 1
    print("Vous avez perdu. L'ordinateur prends {} allumettes.".format(nb_allumettes_ordinateur))
    print("Vous prenez donc forcément la dernière")
    return 1
  else:
    nb_allumettes_ordinateur = N % 6
    if(nb_allumettes_ordinateur == 0):
      nb_allumettes_ordinateur = random.randint(1, 3)
      print("L'ordinateur prends {} allumettes.".format(nb_allumettes_ordinateur))
    N = N - nb_allumettes_ordinateur
    return N

def game():
  N = 21
  a = input("taper 1 pour jouer solo, taper 2 pour jouer a deux:")
  if (a == "2"):
    j1 = input("entrer le nom du joueur 1:")
    j2 = input("entrer le nom du joueur 2:")
    while(N >= 1):
      print("Allumettes disponibles: " + " | " * N)
      t1 = player_one_turn(N,j1)
      if t1 <= 0 or t1 == 1:
        break;
      elif (t1 != 0 and t1 != 1):
        N = t1
      print("Allumettes disponibles: " + " | " * N)
      t2 = player_two_turn(N,j2)
      if t2 <= 0 or t2 == 1:
        break;
      elif (t2 != 0 and t2 != 1):
        N = t2
  elif (a == "1"):
    j1 = input("entrer le nom du joueur 1:")
    while(N >= 1):
      print("Allumettes disponibles: " + " | " * N)
      t1 = player_one_turn(N,j1)
      if t1 <= 0 or t1 == 1:
        break;
      elif (t1 != 0 and t1 != 1):
        N = t1
      print("Allumettes disponibles: " + " | " * N)
      bt = ordinateur_turn(N)
      if (bt <= 0 or bt == 1):
        break;
      elif (bt != 0 and bt != 1):
        N = bt
  else:
    print("erreur")
game()
