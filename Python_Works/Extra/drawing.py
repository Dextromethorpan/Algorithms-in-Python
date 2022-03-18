# # Matrices

# r1=[1,2,3]
# r2=[4,5,6]
# r3=[7,8,9]

# matrix=[r1,r2,r3]

# def print_matrix(m):
#     if m == []:
#         return
#     num_rows=len(m)
#     num_cols=len(m[0])
#     for row in m:
#         line_to_print = ""
#         for num in row:
#             line_to_print += str(num) + " "
#         print(line_to_print)


# def create_matrix(m,n):
#     my_matrix=[]
#     for i in range(m):
#         my_row=[]
#         for j in range(n):
#             my_row.append(0)
#         my_matrix.append(my_row)
#     return my_matrix
nums=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(nums)-2,-1,-1):
    print(i)


