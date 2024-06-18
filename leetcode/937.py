# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        
        for log in logs:
            key = log.split(" ")[0]
            value = " ".join(log.split(" ")[1:])
            
            if value.replace(" ", "").isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([key, value])
        
        letter_logs.sort(key=lambda x: (x[1], x[0]))
        letter_logs = [" ".join(log) for log in letter_logs]

        return letter_logs + digit_logs
    

class Solution2:
    """
    letters, digits 두 종류의 문자열만 존재한다.
    letters content > letters identifier > digits 우선순위로 문자열을 정렬해 반환한다.

    identifier를 기준으로 letters, digits 문자열을 구분하고
    (정렬한 letters + digits 문자열은 처음에 주어진 digits 문자열) 순서로 반환한다.
    """
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []

        # 각 문자열을 순회하면서
        for log in logs:
            # 문자열의 content가 숫자로만 이루어진 경우
            if log.split()[1].isdigit():
                digit_logs.append(log)  # digit 리스트에 추가
            else:
                letter_logs.append(log)  # letter 리스트에 추가
        
        # letter 리스트에 있는 문자열은 content > identifier 순서로 오름차순 정렬
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        # letter, digit 순서대로 반환
        return letter_logs + digit_logs
    

# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
sol = Solution()
out = sol.reorderLogFiles(logs)
print("out:", out)