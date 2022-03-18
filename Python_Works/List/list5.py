#Chapitre 4
#Exercises 4.5
#Ecrivez une fonction qui prend une liste L
#(dont la longueur sera denotee par n dans 
# la suite) de nombres en parametre et qui 
#effectue l'algorithme suivante: 
#-Dans une nouvelle liste L2 de meme longueur
# que L, recopier les deux premiers éléments
# de L aux memes cases de L2.
#-Pour chaque entier i entre 2 et n-1
# -Stocker dans la ie case de L2 la somme des 
#  éléments de L en positions (i-1) et (i-2)
# -Renvoyer L2

L=[1,2,3,4,5,6,7,8,9]

def f1(L):
    L2=[]
    L2.append(L[0])
    L2.append(L[1])
    for i in range(len(L)-1):
        L2.append(L[i]+L[i+1])
    return L2

#print(f1(L))

#f1() recibe una lista y retorna otra lista L2.
#L2 tiene las siguientes características:
#-L2[0]=L[0]
#-L2[1]=L[1]
#-L2[i]=L[i-1]+L[i-2] con i>=2