"""
Divide and Conquer principle
Time Complexity: O(nlogn) -> Worst case
Best case - O(logn) -> when array is sorted.
This algorithm assumes array is already sorted.
Divide the array exactly half and checking whether element lies in which portion of the data.
"""


def binary_search(arr, element):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return arr[mid]
        elif element < arr[mid]:
            high = mid
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 3))
    print(binary_search([1, 2, 3, 4, 5], 7))
