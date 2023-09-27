import numpy as np

import example_matrices

def main():
    print("Hello, Matrix to RAPID code!!")
    matrix = example_matrices.simple_shapes_matrix
    for row in matrix:
        print(''.join(map(str, row)))

if __name__ == "__main__":
    main()