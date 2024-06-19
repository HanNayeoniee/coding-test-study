# 5. Longest Panlindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# 문제 풀이 해설: https://www.youtube.com/watch?v=XYQecbcd6_c


class Solution:
    """
    문자열의 팰린드롬 여부를 판단할 때는 아래 두가지 방법이 있다.
    1) brute force
        문자열의 처음부터 시작해 끝자리를 한칸씩 늘려가면서 s == s[::-1] 인지 확인
    2) 가운데부터 시작해 좌우 한칸씩 늘려가면서 확인
        가운데 문자열을 기준으로 왼쪽, 오른쪽 문자가 동일하면 한칸씩 늘려간다.
    
    1번은 너무 오래 걸리므로 2번으로 풀이한다.
    팰린드롬 문자열은 홀수, 짝수 길이 모두 가능하므로 이 점에 유의한다.
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2  or s == s[::-1]:
            return s
        
        res = ""
        res_len = 0
            
        for i in range(len(s)):
            # 길이가 홀수인 경우
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                l -= 1
                r += 1
            
            # 길이가 짝수인 경우
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                l -= 1
                r += 1
              
        return res
    
    
class Solution2:
    """
    Solution1에서 겹치는 부분을 함수로 만든 코드
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2  or s == s[::-1]:
            return s
        
        res = ""
        res_len = 0
        
        def get_str(s, res, res_len, l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                l -= 1
                r += 1
            
            return res, res_len
            
        
        for i in range(len(s)):
            # 길이가 홀수인 경우                
            res, res_len = get_str(s, res, res_len, i, i)
            # 길이가 짝수인 경우
            res, res_len = get_str(s, res, res_len, i, i+1)
                    
        return res
    
    
