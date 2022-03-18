#Chapitre 4 
#Exercises 4.2
#En supposant que max est un entier positief 
#et que b est un nombre réel(float), que 
#renverra la fonction suivante?

def f(max,b):
    resultat=[]
    n=1
    for i in range(max):
        resultat.append(n)
        n=n*b
    return resultat


#f(max,b) retorna la potencia de un numero
#b es el numero al cual multiplicamos tantas
#veces como max

#print(f(3,3))

#Para que f(max,b) retorne el factorial de 
#b, deberia pasar que max=b.

def f(b):
    resultat=[]
    n=1
    for i in range(b):
        i=i+1
        n=n*i
        resultat.append(n)     
    return resultat

#print(f(3))

