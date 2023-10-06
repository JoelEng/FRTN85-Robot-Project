from image_processing import image_processing
from matrix_to_points import matrix_to_points
from points_to_rapid import points_to_rapid

def main():
    image_matrix = image_processing()
    path_list = matrix_to_points(image_matrix)
    points_to_rapid(path_list)

main()