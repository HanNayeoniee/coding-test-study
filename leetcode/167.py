# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    """
    투포인터 접근법
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i, len(numbers)-1
            
            while l != r:
                if numbers[l]+numbers[r] < target:
                    l += 1
                elif numbers[l]+numbers[r] > target:
                    r -= 1
                else:
                    return [l+1, r+1]