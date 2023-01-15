from typing import List
"""
123
456
789

Pseudo Code:
Step 1: Get the size of the first row.
Step 2: Point two variables point to row and column.
Step 3: Transpose matrix - row to column.
Step 4: Reverse matrix 
"""


def turn_90(input_array:List[List:int]) -> None:
    # Transpose
    array_size = len(input_array)
    for i in range(array_size):
        for j in range(i):
            input_array[i][j], input_array[j][i] = input_array[j][i], input_array[i][j]

    # Reverse
    for i in range(array_size):
        input_array[i] = input_array[i][::-1]

    print(input_array)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turn_90(matrix)
