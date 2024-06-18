# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/


from typing import List
import re
from collections import Counter

class Solution:
    """
    paragraph를 모두 소문자로 변환하고, 공백 기준으로 분리한 후, banned에 없는 단어만 남긴다.
    collections.Counter를 사용해 가장 많이 등장한 단어 1개만 반환한다.    
    """
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        words = [word for word in words if word not in banned]

        # 위의 두 줄을 아래 한줄로 쓸 수 있음
        # words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        c = Counter(words)
        return c.most_common()[0][0]        


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

sol = Solution()
out = sol.mostCommonWord(paragraph, banned)
print(out)