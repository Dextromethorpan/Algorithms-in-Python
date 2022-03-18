# Chapitre 5
# Ecrivez une fonction sumMat(a,b) qui calcule et renvoie une matrice result - la somme des matrices a et b: 
# result(i,j)=a(i,j)+b(i,j) 

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

def init_matrix_1(m,n):
    my_matrix=[]
    for i in range(m):
        my_row = []
        for j in range(n):
            my_row.append(0)
            if j==i:
                my_row[j]=1
        my_matrix.append(my_row)
    return my_matrix


def sumMat(a,b,resultat):
    for i in range(len(resultat)):
        for j in range(len(resultat[0])):
            resultat[i][j]=a[i][j]+b[i][j]
    return resultat

def print_mat(m):
    if m == []:
        return
    for row in m:
        line_to_print = ""
        for num in row:
            line_to_print += str(num) + " "
        print(line_to_print)



M1=init_matrix(3,3)
M2=init_matrix_1(3,3)
M3=init_matrix(3,3)
M4=sumMat(M1,M2,M3)
print_mat(M4)











