from random import randint
def operalea(a,b,r1,r2,method):
	if r1!=0 and r2!=0:
		k=randint(1,3)
	else:
		if b%a==0:
			c=a
			a=b
			b=c
		if a!=b:
			k=randint(1,4)
		else:
			k=randint(2,4)
	if k==1:
		method=method+str(max(a,b))+"-"+str(min(a,b))+"\n"
		return abs(a-b),method
	elif k==2:
		method=method+str(a)+"+"+str(b)+"\n"
		return a+b,method
	elif k==3:
		method=method+str(a)+"*"+str(b)+"\n"
		return a*b,method
	elif k==4:
		method=method+str(a)+"/"+str(b)+"\n"
		return a/b,method
boucle=True
while boucle==True:
	L=[]
	methode=""
	for i in range(1,7):
		L.append(i*randint(1,5)) #L: 6 elements
	J=L[:]
	m=randint(4,5)
	for j in range(m):
		u=randint(0,len(L)-1)
		a=L[u]
		del L[u]
		v=randint(0,len(L)-1)
		b=L[v]
		del L[v]
		ope,methode=operalea(a,b,a%b,b%a,methode)
		L.append(ope)
	if L[len(L)-1]>100 and L[len(L)-1]<1000:
		boucle=False
		print("Les chiffres: ",J)
		print("Valeur: ",L[len(L)-1])
		afficher=input("afficher: \n")
		print(methode)
