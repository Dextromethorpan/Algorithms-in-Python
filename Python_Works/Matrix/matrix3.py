#Chapitre 5
#Exercise 5.4
#Ecrivez une fonction trace(M) qui prend en parametre une matrice M de taille nxn et qui calcule sa trace 
#de la maniere suivante:

#La traza de una matriz es la suma de los elementos de la diagonal
def init_matrix(m,n):
    my_matrix=[]
    for i in range(m):
        my_row = []
        for j in range(n):
            my_row.append(1)
            #if j==i:
            #    my_row[j]=1
        my_matrix.append(my_row)
    return my_matrix

def trace_calcule(M):
    trace=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if j==i:
                trace=M[i][j]+trace
    return trace

M=init_matrix(3,3)
print(trace_calcule(M))

