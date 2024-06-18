# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    
    for char in s:
        if ord(char) == 32:
            answer += ' '
        else:        
            new = int(ord(char) + n)
            if ord('a') <= ord(char) and ord(char) <= ord('z'):    
                if new > ord('z'):
                    answer += chr(new - 26)
                else:
                    answer += chr(new)
            elif ord('A') <= ord(char) and ord(char) <= ord('Z'):    
                if new > ord('Z'):
                    answer += chr(new - 26)
                else:
                    answer += chr(new)
            
    return answer


def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    
    return "".join(s)