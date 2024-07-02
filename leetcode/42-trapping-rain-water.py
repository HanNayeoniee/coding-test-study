# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        
        for i in range(1, len(height)-1):
            l = max(height[:i])
            r = max(height[i+1:])
            
            gap = min(l, r) - height[i]
            if gap > 0:
                result += gap
                
        return result


if __name__ == "__main__":
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    sol = Solution()
    sol.trap(height)