from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    out = []
    res = Counter(nums)
    i = 0
    while i < k:
        out.append(res.most_common()[i][0])
        i = i + 1
    return out