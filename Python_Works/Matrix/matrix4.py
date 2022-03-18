#Chapitre 5
#Exercise 5.5
#On se donne un tableau de nombres, encodé ligne par ligne, sous forme d'une liste dont chaque element
#est lui-meme une liste d'entiers.Par exemple le tableau 
#[[1,2,3],
# [4,5,6],
# [7,8,9]]
#Ecrire une fonction flip(M) qui recoit un tel tableau en parametre, et echange chaque element d'indice i,j 
#avec l'element d'indice n-i-1,m-j-1, ou n est le nombre de lignes et m le nombre de colonnes de M.
#(On utilise ici la convention Python pour les indices, commencant donc a 0)

def init_matrix(m,n):
    my_matrix=[]
    for i in range(m):
        my_row = []
        for j in range(n):
            my_row.append(0)
            #if j==i:
            #    my_row[j]=1
        my_matrix.append(my_row)
    return my_matrix

M=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#La idea es realizar dos rotaciones: una vertical y otra horizontal.
def flip(M):
    m=M[::-1] #rotación horizontal
    m=[row[::-1] for row in m] #rotación vertical
    return m

    
def print_mat(m):
    if m == []:
        return
    for row in m:
        line_to_print = ""
        for num in row:
            line_to_print += str(num) + " "
        print(line_to_print)

M=flip(M)
print_mat(M)
