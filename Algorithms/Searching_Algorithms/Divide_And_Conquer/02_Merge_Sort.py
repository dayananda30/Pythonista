"""
Time Complexity: O(nlogn)
Pros:   Large size List
        Linked List
        External Sorting - Need not to load all data of two external disk to sort.
        Stable - The order of the duplicates are maintained

Cons:   Extra space (not in place sorting)
        No small problem - It is slower for smaller problems, wastes lot of time in recursion.
        Insertion Sort for smaller problem since it is suitable for linked list.


"""


def mergesort(array):
    if len(array) > 1:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]

        # recursion
        mergesort(left_array)
        mergesort(right_array)

        # merge
        i = 0  # index pointing to left array
        j = 0  # index pointing to right array
        k = 0  # index pointing to result array

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i = i + 1
            else:
                array[k] = right_array[j]
                j = j + 1
            k = k + 1

        # append remaining elements of left array
        while i < len(left_array):
            array[k] = left_array[i]
            i = i + 1
            k = k + 1

        # append remaining elements of right array
        while j < len(right_array):
            array[k] = right_array[j]
            j = j + 1
            k = k + 1


array_test = [5, 3, 1, -1, 9]
mergesort(array_test)
print(array_test)
