import cv2
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

coordinates = []

def process_image(image_file):
    img = cv2.imread(image_file)
    #img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    scale_percent = 70  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    print(dim)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # Filter to remove noise
    bilateral = cv2.bilateralFilter(resized, 15, 75, 75)
    # Setting parameter values
    t_lower = 50  # Lower Threshold
    t_upper = 150  # Upper threshold
    # Applying the Canny Edge filter
    edge = cv2.Canny(bilateral, t_lower, t_upper)
    cv2.imwrite("greta_edge.jpeg", edge)
    #cv2.imshow('original', resized)
    #cv2.imshow('edge', edge)
    edge[edge > 0] = 1
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
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
    image_file = 'greta.jpeg'
    image = process_image(image_file)
    return image
    # file_name = 'coordinates.cls'
    # coordinates = []
    # recursive_matrix(image)
    # coordinates_divided = [(x / 3.0, y / 3.0) for x, y in coordinates]
    # write_coordinate_file(coordinates_divided, file_name)

    # Initialize variables to store the current line's starting and ending coordinates
