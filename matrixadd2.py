matrix1 = [
    [2, 4],
    [3, 5]
]

matrix2 = [
    [9, 2], 
    [2, 6]
]

### time to fill matrix
result = add_matrices(matrix1, matrix2)

##the width and height variables are not the same as those in the function
def create_empty_matrix(width, height):
    width = len(result[0])
    height = len(result)
    result = []
    ##initialize the resulting matrix
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            sum = matrix1[i][j] + matrix2[i][j]
            result[i][j] = sum
    return result

##next line defines the width and height outside the function
create_empty_matrix(width, height)
##these are local variables that are local to the function/ DOES NOT BREAK CODE :D
create_empty_matrix(5,3)
matrix = result
print matrix
    ###functions allow us to share code because arguments will not conflict
