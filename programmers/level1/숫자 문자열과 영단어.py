# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = []
    num_dict = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }
    
    rev_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    # 문자열이 key, value에 들어있으면 숫자로 바꾸고
    # 없으면 1자리씩 늘려가며 딕셔너리 안에 존재하는지 확인
    start, end = 0, 1
    while s:
        word = s[start:end]

        if word in num_dict:
            answer.append(word)
            s = s[end:]
            start, end = 0, 1
        else:
            end += 1
            word = s[start:end]
            if word in rev_dict:
                answer.append(rev_dict[word])
                s = s[end:]
                start, end = 0, 1

    return int("".join(answer))


def solution2(s):
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    answer = s
    for key, val in num_dict.items():
        answer = answer.replace(key, val)
    return answer


if __name__ == "__main__":
    s = "one4seveneight"
    # s = "23four5six7"
    # s = "2three45sixseven"
    # s = "123"
    
    res = solution2(s)
    print(res)