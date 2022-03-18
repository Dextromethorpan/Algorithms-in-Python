#Chapitre 5
#Exercise 5.7
#Ecrivez une fonction booleene qui recoit en parametre un tableau de taille nxn et qui repond a la question 
#suivante: existe-t-il une ligne, une colonne, ou une des deux diagonales du tableau qui ne contient que des 
#valeurs identiques?
#Le tableau sera represente par une liste des listes, chacune de ces dernieres representant une ligne du 
#tableau. 

#How to know if two elements are identical in a list
L=[1,2,3,4,4]
def list(L):
    if len(L) != len(set(L)):
        return True
    else:
        return False

M=[[1,2,3,4],[1,6,7,8],[1,10,11,12],[1,14,15,16]]

def two_identical_elements(M):
    n=len(M)
    m=len(M[0])
    L=[]
    P=[]

    for i in range(len(M)):
        if list(M[i][:]):
            return True
    
    for i in range(len(M)):
        if list([row[i] for row in M]):
            return True
    
    for i in range(len(M)):
        for j in range(len(M)):
            if i==j:
                L.append(M[i][j])
            P.append(M[i][m-1])


    if list(L) or list(P):
        return True

    
if two_identical_elements(M):
    print("two identical elements")          

#Note
#No es el mejor codigo en cuanto a tiempos de complejidad.
#Hay demasiados ciclos for.