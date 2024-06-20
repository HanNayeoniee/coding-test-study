# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    """
    brute force
    시간복잡도 O(N^2)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
                            

class Solution2:
    """
    모든 조합을 비교하지 않고 (target-n) 값이 nums에 존재하는지 확인
    시간복잡도 O(N^2)로 첫번째 풀이와 동일하지만, 내부 함수로 구현된 in 연산이 훨씬 빠름
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            pair = target - n
            
            if pair in nums[i+1:]:
                return [i, nums[i+1:].index(pair)+i+1]