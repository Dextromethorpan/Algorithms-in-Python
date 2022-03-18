#Sorting via multiple attributes in Python (key=function)

#Normal Sorting 
def normal_sorting(L):
    return sorted(L)

#Reverse Option
def reverse_sorting(L):
    return sorted(L,reverse=True)

#Sorting a tuple according to the second value 
def tuple_list_sorting_second_value(L):
    func = lambda x: x[1]
    return sorted(L,key=func)

#Sorting a tuple according to first values 
def tuple_list_sorting_first_value(L):
    func = lambda x: str.casefold(x[0])
    return sorted(L,key=func)
#Sorting a tuple according to both values
def tuple_list_sorting_both_values(L):
    func = lambda x: (x[0],x[1])
    return sorted(L,key=func)


#Multiple Parameters
tuple_list=[('a','4'),('a','3'),('c','1'),('d','3')]
L=[]
L=tuple_list_sorting_both_values(tuple_list)
print(L)
