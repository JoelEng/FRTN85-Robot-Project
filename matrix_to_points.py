import example_matrices

from matplotlib import image as img

simple_matrix = [
    [0,1,1,0,1],
    [1,1,0,0,0],
    [0,1,1,0,1],
    [1,1,0,0,0]
]

def main():
    # Replace matrix with output from image processor
    matrix = example_matrices.simple_shapes_matrix
    image = img.imread("greta_pro.jpg")
    #recursive_matrix(matrix)
    recursive_matrix(image)

def only_zero_neighbours(matrix, x, y):
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]

    return sum(matrix[z][w] for z, w in neighbors if 0 <= z < len(matrix) and 0 <= w < len(matrix[0])) == 0

def recursive_helper(matrix, row, col, path, drawing):
    if (only_zero_neighbours(matrix, row, col)):
        matrix[row][col] = 0
        path.append((row, col))
        drawing.append(path)
        #print(row,col)
        #print()
    else:
        matrix[row][col] = 0
        path.append((row, col))
        #print(row, col)

        if col < len(matrix[0]):
            if matrix[row][col+1]:
                recursive_helper(matrix, row, col+1, path, drawing)

        if row < len(matrix)-1:
            if matrix[row+1][col]:
                recursive_helper(matrix, row+1, col, path, drawing)
        
        if col < len(matrix[0]) and row < len(matrix)-1:
            if matrix[row+1][col+1]:
                recursive_helper(matrix, row+1, col+1, path, drawing)
        
        if row < len(matrix)-1 and col > 0:
            if matrix[row+1][col-1]:
                recursive_helper(matrix, row+1, col-1, path, drawing)

def recursive_matrix(matrix):
    SMALLEST_PATH = 2
    drawing = list()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
                if matrix[row][column]:
                    path = list()
                    recursive_helper(matrix, row, column, path, drawing)

    sorted_list = sorted(drawing, key=len, reverse=True)
    filtered_list = filter(lambda x: len(x) > SMALLEST_PATH, sorted_list)

    return filtered_list

if __name__ == "__main__":
    main()