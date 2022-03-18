#Chapitre 4
#Exercise 4.4 
# Adaptez la fonction suivante pour qu'au 
# retour de la fonction, chaque élément de
# L est remplacé par la somme de tous les
# éléments qui le précédaient dans la liste.

def f(L):
    resultat=[]
    n=0
    for i in range(len(L)):
       n=n+L[i]
       resultat.append(n)   
    return resultat

M=[1,2,3,4,5]

print(f(M))

#f(M) convierte la siguente lista 
#[1,2,3,4,5]->[1,3,6,10,15]