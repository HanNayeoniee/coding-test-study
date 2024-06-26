# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/


from typing import List

class Solution:
    """
    brute force 방법으로 시간초과
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i != j:
                    if total != 0 and nums[j] != 0:
                        total *= nums[j]
                    else:
                        total = 0
                        break
            output.append(total)
        
        return output


class Solution2:
    """
    prefix 곱과 suffix 곱을 구해 곱한다.
    prefix, suffix 곱을 구해 각각 다른 리스트에 저장했다.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ff, bb = 1, 1
        front, back = [ff], [bb]
        
        # prefix 곱 구하기
        for i in range(len(nums)-1):
            ff *= nums[i]
            front.append(ff)

        # suffix 곱 구하기
        for i in range(len(nums)-1, 0, -1):
            bb *= nums[i]
            back.append(bb)
        
        # 거꾸로 저장되기 때문에 뒤집는다.
        back = back[::-1]

        # 각 요소별로 prefix * suffix
        output = []
        for i in range(len(nums)):
            output.append(front[i] * back[i])

        return output
    
class Solution3:
    """
    prefix 곱과 suffix 곱을 구해 곱한다.
    추가 저장공간을 사용하지 않았다.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        out = []

        # 왼쪽 곱셉
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셉
        for i in range(len(nums)-1, -1, -1):
            out.append(p)
            p = p * nums[i]
        
        return out