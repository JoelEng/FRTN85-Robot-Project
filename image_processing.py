import cv2
import sys
import numpy
import csv
numpy.set_printoptions(threshold=sys.maxsize)

def process_image(image_file):
    img = cv2.imread(image_file)
    #img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    scale_percent = 100  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
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
    #cv2.imshow('original', resized)
    #cv2.imshow('edge', edge)
    edge[edge > 0] = 1
    print(edge.shape)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return edge

def get_coordinates_from_binary_image(image):
    coordinates = []
    print(image.shape)
    width, height = image.shape

    for x in range(width):
        for y in range(height):
            pixel = image[x, y]
            if pixel == 1:
                coordinates.append((x, y))
    return coordinates

def write_coordinate_file(coordinates, file_name):
    with open(file_name, 'w') as coordinate_file:
        for x, y in coordinates:
            coordinate_file.write(f"{x} {y}\n")

if __name__ == '__main__':
    image_file = 'greta.jpeg'
    image = process_image(image_file)
    coordinates = get_coordinates_from_binary_image(image)
    coordinate_file_name = 'coordinates.cls'
    write_coordinate_file(coordinates, coordinate_file_name)
    csv_file_name = 'coordinates.csv'
    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['x', 'y'])  # Header row
        for x, y in coordinates:
            csv_writer.writerow([x, y])

