# Python
# -*- coding:UTF-8 -*-

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# 문제 20 유효한 괄호 : 괄호로 된 입력값이 올바른지 판별하라

# 입력
input = '()[]{}' # 출력 true

# 풀이 1 : 스택 일치 여부 판별 

def isValid(s):
    # (, [, {는 스택에 push하고, }, ], )를 만날 때 스택에서 pop한 결과가 매핑 테이블 결과와 매칭되는지 확인
    # 매핑 테이블을 만들어 놓고 테이블에 존재하지 않으면 무조건 푸시, 아니면 false 리턴하도록 
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        # 이하와 같이 예외 처리를 잊지 말자
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0

print(isValid(input)) 