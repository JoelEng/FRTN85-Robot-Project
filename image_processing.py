import cv2
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

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
    edge[edge > 0] = 1
    return edge

def image_processing():
    image_file = 'greta.jpeg'
    image = process_image(image_file)
    return image
