def searchRange(nums: List[int], target: int) -> List[int]:
    out = []
    for index, item in enumerate(nums):
        if item == target:
            out.append(index)

    if len(out) == 0:
        return [-1,-1]
    elif len(out)==1:
        return [out[0],out[0]]
    else:
        return [out[0],out[len(out)-1]]

searchRange([1, 3, 7, 5, 4, 3], 3)
