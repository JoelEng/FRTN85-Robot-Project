MIN_VALUE = 200
MAX_VALUE = 30

def only_zero_neighbours(matrix, x, y):
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]

    return sum(matrix[z][w] for z, w in neighbors if 0 <= z < len(matrix) and 0 <= w < len(matrix[0])) <= MAX_VALUE

def recursive_helper(matrix, row, col, path, drawing):
    if (only_zero_neighbours(matrix, row, col)):
        matrix[row][col] = 0
        path.append((row, col))
        drawing.append(path)
    else:
        matrix[row][col] = 0
        path.append((row, col))

        try:
            if matrix[row][col+1] >= MIN_VALUE:
                recursive_helper(matrix, row, col+1, path, drawing)
        except IndexError:
            pass

        try:
            if matrix[row+1][col+1] >= MIN_VALUE:
                recursive_helper(matrix, row+1, col+1, path, drawing)
        except IndexError:
            pass
    
        try:
            if matrix[row+1][col] >= MIN_VALUE:
                recursive_helper(matrix, row+1, col, path, drawing)
        except IndexError:
            pass
    
        try:
            if matrix[row+1][col-1] >= MIN_VALUE:
                recursive_helper(matrix, row+1, col-1, path, drawing)
        except IndexError:
            pass

        try:
            if matrix[row][col-1] >= MIN_VALUE:
                recursive_helper(matrix, row, col-1, path, drawing)
        except IndexError:
            pass

        # try:
        #     if matrix[row-1][col-1] >= MIN_VALUE:
        #         recursive_helper(matrix, row-1, col-1, path, drawing)
        # except IndexError:
        #     pass
    
        # try:
        #     if matrix[row-1][col] >= MIN_VALUE:
        #         recursive_helper(matrix, row-1, col, path, drawing)
        # except IndexError:
        #     pass

        # try:
        #     if matrix[row-1][col+1] >= MIN_VALUE:
        #         recursive_helper(matrix, row-1, col+1, path, drawing)
        # except IndexError:
        #     pass

def matrix_to_points(matrix):
    SMALLEST_PATH = 2
    drawing = list()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
                if matrix[row][column] >= MIN_VALUE:
                    path = list()
                    recursive_helper(matrix, row, column, path, drawing)

    sorted_list = sorted(drawing, key=len, reverse=True)
    filtered_list = filter(lambda x: len(x) > SMALLEST_PATH, sorted_list)

    unique_sorted_list = []
    [unique_sorted_list.append(x) for x in filtered_list if x not in unique_sorted_list]

    return unique_sorted_list
