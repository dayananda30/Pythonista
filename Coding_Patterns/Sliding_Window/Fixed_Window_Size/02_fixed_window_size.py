from typing import List


def fixed_sliding_window(arr: List[int], k: int) -> List[int]:
    subarray_sum = sum(arr[:k])
    result = [subarray_sum]
    for i in range(1, len(arr) - k + 1):
        subarray_sum = subarray_sum - arr[i - 1]
        subarray_sum = subarray_sum + arr[i + k - 1]

        result.append(subarray_sum)
    return result
