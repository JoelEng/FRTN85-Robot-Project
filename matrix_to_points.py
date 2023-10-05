import example_matrices

simple_matrix = [
    [0,1,1,0,1],
    [1,1,0,0,0],
    [0,1,1,0,1],
    [1,1,0,0,0]
]

def main():
    # Replace matrix with output from image processor
    matrix = example_matrices.simple_shapes_matrix
    for row in matrix:
        print(''.join(map(str, row)))
    recursive_matrix(matrix)

def only_zero_neighbours(matrix, x, y):
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]

    return sum(matrix[z][w] for z, w in neighbors if 0 <= z < len(matrix) and 0 <= w < len(matrix[0])) == 0

def recursive_helper(matrix, row, col):
    if (only_zero_neighbours(matrix, row, col)):
        matrix[row][col] = 0
        print(row,col)
        print()
    else:
        matrix[row][col] = 0
        print(row, col)

        if col < len(matrix[0]):
            if matrix[row][col+1]:
                recursive_helper(matrix, row, col+1)

        if row < len(matrix)-1:
            if matrix[row+1][col]:
                recursive_helper(matrix, row+1, col)
        
        if col < len(matrix[0]) and row < len(matrix)-1:
            if matrix[row+1][col+1]:
                recursive_helper(matrix, row+1, col+1)
        
        if row < len(matrix)-1 and col > 0:
            if matrix[row+1][col-1]:
                recursive_helper(matrix, row+1, col-1)

def recursive_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
                if matrix[row][column]:
                    recursive_helper(matrix, row, column)

if __name__ == "__main__":
    main()