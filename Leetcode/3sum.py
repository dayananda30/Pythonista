from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    i = 0
    visted_index, output = [], []
    while i < len(nums) - 2:
        j = i + 1
        while j < len(nums) - 1:
            k = j + 1
            if ((nums[i] + nums[j] + nums[k]) == 0) and (i not in visted_index) and (j not in visted_index) and (
                    k not in visted_index):
                visted_index.append([i, j, k])
                tmp = [nums[i], nums[j], nums[k]]
                output.append(tmp)
            j = j + 1
        i = i + 1
    print(output)
    return output


threeSum([-2, 0, 0, 0, 1, 1])
