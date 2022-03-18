# Chapitre 4
#Listes
#Exercises 4.1
#En supposant que L est une liste et que e est un objet quelconque, 
#que renverra la fonction suivante?

L=[1,1,1,1,1,1,1]

def f(L,e):
    n = 0
    for elem in L:
        if elem == e:
            n +=1
    return n

#Esta function permite saber la cantidad 
#de veces que se repite un elemento e.