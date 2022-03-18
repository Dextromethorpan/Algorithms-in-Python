#Chapitre 4

#Exercises 4.7

#La fonction suivante vérifie si, dans une liste
#L donnée, les éléments d’indice impair
#sont triés entre eux dans l’ordre croissant. 
#Écrivez une fonction qui dira si les éléments 
#de valeur paire sont triés dans l’ordre 
#croissant.

L=[1,2,3,4,6,6,10]

def indices_impairs_tries(L):
    trie = True
    i = 0
    while trie and i < len(L)-2:
        if L[i] > L[i+2]:
            trie = False
        i += 2
    return trie

if indices_impairs_tries(L):
    print("los impares son crecientes")
else:
    print("los impares no son crecientes")

