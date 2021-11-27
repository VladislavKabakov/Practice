print("Input the number of rows in matrix A")
A_rows = int(input())
print("Input the number of columns in matrix A")
A_columns = int(input())

#Заполнение матрицы
A = []
row = []
for _ in range(A_rows):
    for _ in range(A_columns):
        elem = int(input())
        row.append(elem)
    A.append(row)
    row = []
    
def max_of_column(matr): #Ищет максимальную ширину каждого столбца
    arr_of_max = []
    max_len = 0
    for ind in range(A_columns):
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

print_matrix(A)
