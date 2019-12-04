def AnnonceJoueurs():
	NbJoueurs=0
	while NbJoueurs <1 or NbJoueurs>4:
		NbJoueurs=input("Entrez le nombre de joueurs(maxi 4)")
		try:
			NbJoueurs=int(NbJoueurs)
			assert NbJoueurs >= 1 and NbJoueurs <= 4
			except AssertionError:
				print("Il doit y avoir entre 1 et 4 joueurs")
				NbJoueurs=0
			except ValueError:
				print("Entrez un nombre de joueurs")
				NbJoueurs=0
	L=[]
	for k in range (NbJoueurs):
		L.append(input("entrez le nom du joueur", k+1))
	return(NbJoueurs,L)
		
		
	