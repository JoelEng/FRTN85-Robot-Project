import numpy as np

import basic_heart_matrix

def main():
    print("Hello, Matrix to RAPID code!!")
    matrix = basic_heart_matrix.heart_matrix
    for row in matrix:
        print(''.join(map(str, row)))

if __name__ == "__main__":
    main()