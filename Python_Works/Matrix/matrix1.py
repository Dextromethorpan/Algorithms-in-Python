# Chapitre 5 

# Ex 5.1
# Ecrivez une fonction init_mat(m,n) et une fonction print_mat(M)
# la funcion int_mat(m,n) inicializa una matriz de mxn con indices cero
# la funcion print_mat(M) imprime una matrix

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


def print_mat(m):
    if m == []:
        return
    for row in m:
        line_to_print = ""
        for num in row:
            line_to_print += str(num) + " "
        print(line_to_print)

M=init_matrix(4,4)
#print_mat(M)

# Como puedo crear una matriz diagonal en Python? 
def diagonal(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if j==i:
                M[i][j]=1
    return M

#M1=diagonal(M)
#print_mat(M1)

# Ex 5.2 
# Que fait la fonction suivante?
def symetrie(m):
    sym = True 
    i=0
    n=len(m)
    while i < n and sym:
        j=0
        while j < i and sym:
            if m[i][j] != m[j][i]:
                sym = False
            j+=1
        i+=1
    return sym

if(symetrie(M)):
    print("Symmetric Matrix")
else:
    print("Not symmetric Matrix")
