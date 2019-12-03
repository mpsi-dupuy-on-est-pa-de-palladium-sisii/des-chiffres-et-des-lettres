from fonctions import Generateur

def LancementJeu():
	v=input("Tapez 1 pour jouer, 0 pour quitter")
	try:
		v=int(v) #on tente de convertir v en entier
		assert v==1 or v==0 #on teste si v est different de 1 ou 0 si il est entier
	except AssertionError: #si v est pas 0 ou 1
		print("Nombre non reconnu")
		v=2
	except ValueError:#si v est pas un entier
		print("Ceci n'est pas un nombre")
		v=2
	return (v)

def AffichageReponsePossible():
	v=input("Appuyez sur entrée pour afficher une solution possible")
	soluce=open("solution.txt","r") #on ouvre le fichier ou est stocké la soluce
	K=[]
	for L in soluce.readlines():
		K.append(L.strip()) #on construit une liste de chaque ligne de la soluce sans les \n
	return K


jeu_actif=1
while jeu_actif != 0:
	jeu_actif=LancementJeu()
	if jeu_actif==2 or jeu_actif==0:
		continue
	objectif,liste=Generateur()
	print(objectif)
	print(liste)
	L=AffichageReponsePossible()
	print(L)


		


