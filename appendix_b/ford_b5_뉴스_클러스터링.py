import collections
import re


# 입력
str11 = "FRANCE"
str12 = "french"
str21 = "handshake"
str22 = "shake hands"
str31 = "aa1+aa2"
str32 = "AAAA12"
str41 = "E=M*C^2"
str42 = "e=m*c^2"


# 출력
a1 = 16384
a2 = 65536
a3 = 43690
a4 = 65536


def solution(str1, str2):
    str1s = [
        str1[i:i+2].lower()
        for i in range(len(str1)-1)
        if re.findall('[a-z]{2}', str1[i:i+2].lower())
    ]
    str2s = [
        str2[i:i+2].lower()
        for i in range(len(str2)-1)
        if re.findall('[a-z]{2}', str2[i:i+2].lower())
    ]
    intersection = sum((collections.Counter(str1s) &
                        collections.Counter(str2s)).values())
    union = sum((collections.Counter(str1s) |
                 collections.Counter(str2s)).values())
    
    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)


print(solution(str11, str12))
print(solution(str11, str12) == a1)
print(solution(str21, str22))
print(solution(str21, str22) == a2)
print(solution(str31, str32))
print(solution(str31, str32) == a3)
print(solution(str41, str42))
print(solution(str41, str42) == a4)
