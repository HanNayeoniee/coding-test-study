# 561. Array Partition
# https://leetcode.com/problems/array-partition/

from typing import List

class Solution:
    """
    nums를 오른차순 정렬한 후, 2자리씩 min값의 합을 구한다.
    2자리씩 min값의 합 = 인덱스가 짝수인 숫자의 합 (0, 2, 4 ...)
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
  
        return sum([nums[i] for i in range(0, len(nums), 2)])