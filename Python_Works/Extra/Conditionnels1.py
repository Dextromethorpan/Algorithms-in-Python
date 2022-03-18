#Chapitre 2
#Exercises 2.1
#Que font les fonctions suivantes? Testez avec des exemples

#function1() sirve para saber si un numero es par o impar
def function1(n) :
    if n%2==0 :
        return True
    return False

def function2(n) :
    result = n
    if n%2==0 :
        result = result/2
    else :
        result = result-1
        result = result/2
    return result

def function3(n) :
    if n%3==0 and not n%2==0:
        res = True
    elif n%4==0 and n%7==0:
        res = True
    else:
        res = False
    return res

