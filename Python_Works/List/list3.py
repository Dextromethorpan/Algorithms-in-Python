#Chapitre 4
#Exercise 4.3
#Adaptez la fonction suivante pour qu'elle 
#renvoie l'element minimal de la liste 
#donnée en parametre

L=[9,8,7,6,5,4,3,2,1]


#f(L) devuelve el minimo de una lista
def f(L):
    resultat=L[0]
    for elem in L:
        if elem < resultat:
            resultat = elem
    return resultat

print(f(L))