"""
CH19. 73_UTF-8_Validation.py
"""

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# 입력 1
data1 = [197, 130, 1] # 1100 0101, 1000 0010, 0000 0001
# 첫 바이트가 110~ 이므로 2바이트 문자.
# 2바이트 문자 뒤에 오는 1바이트 문자. 정상

# 출력 1
output1 = True


# 입력 2
data2 = [235, 140, 4] # 1110 1011, 1000 1100, 0000 0100
# 첫 바이트가 1110~ 이므로 3바이트 문자임. 그러나 세번째 바이트가 00~이므로 비정상.

# 출력 2
output2 = False


'''
* 참고
바이트 수 1바이트   2바이트    3바이트    4바이트
    1   0~      
    2   110~    10~      10~
    3   1110~   10~      10~
    4   11110~  10~      10~       10~
'''


# --------------------------------------------------
def validUtf8(data):
    def check(size):
        for i in range(start + 1, start + size + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True
    
    start = 0
    while start < len(data):
        first = data[start]
        if (first >> 3) == 0b11110 and check(3):
            start += 4
        elif (first >> 4) == 0b1110 and check(2):
            start += 3
        elif (first >> 5) == 0b110 and check(1):
            start += 2
        elif (first >> 7) == 0:
            start += 1
        else:
            return False
    return True


print(validUtf8(data1))
print(validUtf8(data1) == output1)
print(validUtf8(data2))
print(validUtf8(data2) == output2)
