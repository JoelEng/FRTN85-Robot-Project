def only_zero_neighbours(matrix, x, y):
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]

    return sum(matrix[z][w] for z, w in neighbors if 0 <= z < len(matrix) and 0 <= w < len(matrix[0])) == 0

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
    PATH_CUTOFF = 40
    drawing = list()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
                if matrix[row][column]:
                    path = list()
                    recursive_helper(matrix, row, column, path, drawing)

    filtered_list = filter(lambda x: len(x) > SMALLEST_PATH, drawing)

    longest_paths = [x for x in filtered_list if len(x) >= PATH_CUTOFF]

    sorted_path = sorted(longest_paths, key=len, reverse=True)

    new_paths = sorted_path + filtered_list

    unique_sorted_list = [x for x in new_paths if x not in unique_sorted_list]

    return unique_sorted_list

# def main():
#     matrix_to_points(img.imread("greta_pro.jpg"))

# main()