from random import randint

#ecrasage du fichier
def Init():
    ecraser=open("solution.txt","w")
    ecraser.close()

#Fonction qui cree une liste
def CreationListe():
    L=[]
    for k in range (1,7):
        L.append(k*randint(1,10))
    return (L)

#fonction pour faire une operation aleatoire
def Operation(a,b):
    solution=open("solution.txt","a")
    n=randint(1,4)
    if n == 1: #division
        if a%b == 0:
            solution.write(str(a)+"/"+str(b)+"="+str(a//b)+"\n")
            return (a//b)
        elif b%a == 0:
            solution.write(str(b)+"/"+str(a)+"="+str(b//a)+"\n")
            return (b//a)
        else :
            n=randint(2,4)
    if n == 2: #soustraction
        if a>b:
            solution.write(str(a)+"-"+str(b)+"="+str(a-b)+"\n")
            return (a-b)
        else: 
            solution.write(str(b)+"-"+str(a)+"="+str(b-a) +"\n")
            return (b-a)
    if n == 3: #multiplication
        solution.write(str(b)+"x"+str(a)+"="+str(a*b)+"\n")
        return (a*b)

    else : #addition
        solution.write(str(b)+"+"+str(a)+"="+str(a+b)+"\n")
        return (a+b)
    solution.close()

#Calcul dun resultat possible

def CalculResultat(L):
    K=[]
    for k in L:
        K.append(k) #on cree un liste auxiliaire pour ne pas retourner une liste vide a la fin
    a=randint(0,5) #on choisit d'abord un element au hasard sinon on sait que on commence par le premier -> triche
    resultat=K[a]
    K.remove(K[a])
    for k in range (5):
        a=randint(0,len(K)-1)
        resultat=Operation(resultat,K[a])
        K.remove(K[a])
    return(resultat,L) #on renvoie le resultat et la liste non vide creee au debut

#on affiche la liste et le resultat

def Generateur():
    resultat_affiche=0
    while resultat_affiche<50 or resultat_affiche>1000:
        Init()
        L=CreationListe()
        resultat_affiche,L=CalculResultat(L)
    return(resultat_affiche,L)

