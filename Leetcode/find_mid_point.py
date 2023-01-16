from typing import List

"""
[10,5,2,3,3,2,10,5]

"""


def find_mid_point(input_arr: List) -> int:
    for i in range(len(input_arr)):
        for j in range(i+1, len(input_arr)):
            if sum(input_arr[:i]) == sum(input_arr[i:]):
                print("Mid point is: {}".format(i))
            break


find_mid_point([10, 5, 2, 3, 3, 2, 10, 5])
