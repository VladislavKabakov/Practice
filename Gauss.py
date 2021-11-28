print("Input size of matrix A (square)")
size_of_A = int(input())


A = []
row = []
for _ in range(size_of_A):
    for _ in range(size_of_A):
        elem = float(input())
        row.append(elem)
    A.append(row)
    row = []

B = []
print("Input the vector B")
for _ in range(size_of_A):
    elem_b = float(input())
    B.append(elem_b)

mat_A = A.copy()
vec_B = B.copy()
X = [0 for _ in range(size_of_A)]

print("Solving A * X = B...")

#Преобразование исходной матрицы А и вектора В
for ind_row in range(0, size_of_A):
    A_diag = mat_A[ind_row][ind_row]
    if A_diag == 0:
        print("Can't solve")
        break

    for ind_el in range(ind_row, size_of_A):
        mat_A[ind_row][ind_el] /= A_diag
    vec_B[ind_row] /= A_diag

    for ind_next in range(ind_row + 1, size_of_A):

        A_next = A[ind_next][ind_row]
        for ind_col in range(ind_row, size_of_A):
            mat_A[ind_next][ind_col] -= A_next * mat_A[ind_row][ind_col]
        vec_B[ind_next] -= A_next * vec_B[ind_row]

#Поиск переменных
for row_ind in range (size_of_A - 1, -1, -1):
    X[row_ind] = vec_B[row_ind]
    for ind_el in range(row_ind + 1, size_of_A):
        X[row_ind] -= mat_A[row_ind][ind_el] * X[ind_el]


print("The answer is:")
print("X =", "{", X, "}")


        
    
   
    

    
    

    

   
    

        
    
    
        
        


















'''def max_of_column(matr): #Ищет максимальную ширину каждого столбца
    arr_of_max = []
    max_len = 0
    for ind in range(size_of_A):
        for ind_row in matr:
            max_len = max(max_len,len(str(ind_row[ind])))
        arr_of_max.append(max_len)
        max_len = 0
    return arr_of_max

columns_width = max_of_column(A)

def print_matrix(matr):
    for row in matr:
        row_str = ""
        for ind_el in range(len(row)):
            row_str += str(row[ind_el]).ljust(columns_width[ind_el]) + " "
        print(row_str)

print_matrix(A)'''


