N = 21
j1 = input("entrer le nom du joueur 1")
j2 = input("entrer le nom du joueur 2")
while(N >= 1):
    print("Allumettes disponibles: " + " | " * N)

    print("c'est à",j1,"de jouer")
    nb_allumettes_joueur = -1
    while(not nb_allumettes_joueur in range(1,4)):
        nb_allumettes_joueur = int(input("Combien d'allumettes souhaitez vous retirer ? (entre 1 et 3) : "))
    N = N - nb_allumettes_joueur
    if(N < 0):
       print(j1,"Vous avez perdu !")
       break;
    elif(N == 1):
        print(j1,"Vous avez gagné !")
        break;
    print("Allumettes disponibles: " + " | " * N)
    print("c'est à",j2,"de jouer")
    nb_allumettes_joueur = -1
    while(not nb_allumettes_joueur in range(1,4)):
        nb_allumettes_joueur = int(input("Combien d'allumettes souhaitez vous retirer ? (entre 1 et 3) : "))
    N = N - nb_allumettes_joueur
    if(N < 0):
       print(j2,"Vous avez perdu !")
       break;
    elif(N == 1):
        print(j2,"Vous avez gagné !")
        break;
    