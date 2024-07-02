# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict

class Solution:
    """
    {각 문자열을 알파벳 순으로 정렬한 결과: [원본 문자열]} 형태의 딕셔너리로 저장
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            words[key].append(s)
        
        return list(words.values())
    

# sorted 활용 예제
a = ['ced', 'cfc', 'abc']
def fn(s):
    return s[0], s[-1]

print(sorted(a, key=fn))
print(sorted(a, key=lambda s: (s[0], s[-1])))