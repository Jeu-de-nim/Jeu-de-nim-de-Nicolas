def player_one_turn(N, j1):
  print("c'est à",j1,"de jouer")
  nb_allumettes_joueur = -1
  while(not nb_allumettes_joueur in range(1,4)):
    nb_allumettes_joueur = int(input("Combien d'allumettes souhaitez vous retirer ? (entre 1 et 3) : "))
  N = N - nb_allumettes_joueur
  if(N <= 0):
    print(j1,"Vous avez gagné !")
    return 0
  elif(N == 1):
    print(j1,"Vous avez perdu !")
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
      print(j2,"Vous avez gagné !")
      return 0
    elif(N == 1):
      print(j2,"Vous avez perdu !")
      return 1
    else:
      return N


def game():
  N = 21
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
game()
