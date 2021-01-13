"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image 
is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def RotateMatrix(matrix: list) -> list:
    if len(matrix) == 0 or len(matrix[0]) != len(matrix):
        return False
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(last):
            offset = i - first
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last-offset][first]

            # bottom -> left
            matrix[last-offset][first] = matrix [last][last-offset]

            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    
    return matrix


    