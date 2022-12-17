"""
Time Complexity : O(N)
Linear Search :
    Searches for a given element present in the array or not in a sequential manner.
    :returns element if present else -1
"""


def linear_search(arr, element):
    for item in arr:
        if item == element:
            return item
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    print(linear_search(arr, 5))
    print(linear_search(arr, 6))
