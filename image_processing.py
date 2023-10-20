import cv2
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

coordinates = []

def process_image(image_file):
    img = cv2.imread(image_file)
    width = 300
    height = 169
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # Filter to remove noise
    bilateral = cv2.bilateralFilter(resized, 15, 75, 75)
    # Setting parameter values
    t_lower = 50  # Lower Threshold
    t_upper = 150  # Upper threshold
    # Applying the Canny Edge filter
    edge = cv2.Canny(bilateral, t_lower, t_upper)
    edge = cv2.flip(edge, 1)
    cv2.imwrite("greta_edge.jpeg", edge)
    edge[edge > 0] = 1
    return edge

def write_coordinate_file(coordinates, file_name):
    with open(file_name, 'w') as coordinate_file:
        for x, y in coordinates:
            if x < 0 and y < 0:
                coordinate_file.write("\n")
            else:
                coordinate_file.write(f"{x} {y}\n")


def only_zero_neighbours(matrix, x, y):
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1),
                 (x + 1, y - 1)]

    return sum(matrix[z][w] for z, w in neighbors if 0 <= z < len(matrix) and 0 <= w < len(matrix[0])) == 0


def recursive_helper(matrix, row, col, first_visit):
    if only_zero_neighbours(matrix, row, col) and not first_visit:
        matrix[row][col] = 0
        print(row, col)
        print()
        coordinates.append((row,col))
        coordinates.append((-1,-1))
    elif not only_zero_neighbours(matrix, row, col):
        matrix[row][col] = 0
        print(row, col)
        coordinates.append((row, col))

        if col < len(matrix[0]):
            if matrix[row][col + 1]:
                recursive_helper(matrix, row, col + 1, False)

        if row < len(matrix) - 1:
            if matrix[row + 1][col]:
                recursive_helper(matrix, row + 1, col, False)

        if col < len(matrix[0]) and row < len(matrix) - 1:
            if matrix[row + 1][col + 1]:
                recursive_helper(matrix, row + 1, col + 1, False)

        if row < len(matrix) - 1 and col > 0:
            if matrix[row + 1][col - 1]:
                recursive_helper(matrix, row + 1, col - 1, False)


def recursive_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column]:
                recursive_helper(matrix, row, column, True)

def image_processing():
    image_file = 'new_greta.jpg'
    image = process_image(image_file)
    return image


    # Initialize variables to store the current line's starting and ending coordinates





