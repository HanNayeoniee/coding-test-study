# 15. 3Sum
# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    """
    세 수의 합이 특정 값이 되는 조합을 중복 없이 구해야 한다.
    숫자 1개를 고정해놓고 투 포인터로 풀이한다.
    """    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            # 투포인터 초기화
            l, r = i+1, len(nums)-1
            while l < r:
                # 세 수의 합이 작으면 왼쪽 포인터를 중앙과 가깝게 이동하고,
                # 합이 크면 오른쪽 포인터를 중앙과 가깝게 이동한다.
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    # 정답 조합을 발견한 경우
                    output.append([nums[i], nums[l], nums[r]])

                    # 세 수의 조합은 중복될 수 없으므로 왼쪽, 오른쪽 포인터 값이 각각 앞뒤로 동일한 경우
                    # 포인터를 가장 중앙쪽으로 이동시켜 정답 조합으로 포함시킨다.
                    while l<r and nums[l]==nums[l+1]:
                        l += 1
                    while l<r and nums[r]==nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return output