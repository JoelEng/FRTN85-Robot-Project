# import example_matrices
# from matplotlib import image as img

def only_zero_neighbours(matrix, x, y):
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]

    return sum(matrix[z][w] for z, w in neighbors if 0 <= z < len(matrix) and 0 <= w < len(matrix[0])) == 0

def iterative(matrix, row, col, path, drawing):
    coord_stack = [(row,col)]

    rows = len(matrix)
    cols = len(matrix[0])

    while(coord_stack):
        coord = coord_stack.pop()
        row = coord[0]
        col = coord[1]

        matrix[row][col] = 0
        path.append((row, col))

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col]:
                    coord_stack.append((new_row, new_col))

    drawing.append(path)

def recursive_helper(matrix, row, col, path, drawing):
    if (only_zero_neighbours(matrix, row, col)):
        matrix[row][col] = 0
        path.append((row, col))
        drawing.append(path)
    else:
        matrix[row][col] = 0
        path.append((row, col))

        try:
            if matrix[row][col+1]:
                recursive_helper(matrix, row, col+1, path, drawing)
        except IndexError:
            pass

        try:
            if matrix[row+1][col+1]:
                recursive_helper(matrix, row+1, col+1, path, drawing)
        except IndexError:
            pass
    
        try:
            if matrix[row+1][col]:
                recursive_helper(matrix, row+1, col, path, drawing)
        except IndexError:
            pass
    
        try:
            if matrix[row+1][col-1]:
                recursive_helper(matrix, row+1, col-1, path, drawing)
        except IndexError:
            pass

        try:
            if matrix[row][col-1]:
                recursive_helper(matrix, row, col-1, path, drawing)
        except IndexError:
            pass

        # try:
        #     if matrix[row-1][col-1]:
        #         recursive_helper(matrix, row-1, col-1, path, drawing)
        # except IndexError:
        #     pass
    
        # try:
        #     if matrix[row-1][col]:
        #         recursive_helper(matrix, row-1, col, path, drawing)
        # except IndexError:
        #     pass

        # try:
        #     if matrix[row-1][col+1]:
        #         recursive_helper(matrix, row-1, col+1, path, drawing)
        # except IndexError:
        #     pass

def matrix_to_points(matrix):
    SMALLEST_PATH = 2
    drawing = list()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
                if matrix[row][column]:
                    path = list()
                    # recursive_helper(matrix, row, column, path, drawing)
                    iterative(matrix, row, column, path, drawing)

    sorted_list = sorted(drawing, key=len, reverse=True)
    filtered_list = filter(lambda x: len(x) > SMALLEST_PATH, sorted_list)

    unique_sorted_list = []
    [unique_sorted_list.append(x) for x in filtered_list if x not in unique_sorted_list]

    for i in range(len(unique_sorted_list)):
        p = []
        [p.append(x) for x in unique_sorted_list[i] if x not in p]
        unique_sorted_list[i] = p

    return unique_sorted_list

# def main():
#     matrix_to_points(img.imread("greta_pro.jpg"))

# main()