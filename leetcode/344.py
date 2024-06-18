# 344. Reverse String
# https://leetcode.com/problems/reverse-string/

from typing import List

class Solution1:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-1-i] = s[n-1-i], s[i]


class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        two pointer를 이용한 swap
        '리턴 없이 내부를 직접 조작하라'고 했으니 문자열 내부를 swap한다
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1