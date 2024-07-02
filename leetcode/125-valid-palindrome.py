# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

class Solution1:
    """
    isalnum()으로 각 문자가 알파벳 혹은 숫자인지 검사
    """
    def isPalindrome(self, s: str) -> bool:
        alphas = []
        for char in s:
            if char.isalnum():
                alphas.append(char.lower())
        
        return alphas == alphas[::-1]
    

import re
class Solution2:
    """
    정규표현식으로 불필요한 문자 필터링
    """
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]