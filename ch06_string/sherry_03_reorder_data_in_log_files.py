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
# from typing import Deque

# 문제 03 로그 파일 재정렬 : 로그의 가장 앞 부분은 식별자이며, 문자로 구성된 로그가 숫자 로그보다 앞에 오고, 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 하며, 숫자 로그는 입력 순서대로 한다.

# 예제
logs = ["digl 8 1 5 l","letl art can","dig2 3 6","let2 own kit dig","let3 art zero"] # ["letl art can%"let3 art zero","let2 own kit dig","digl 8 1 5 l","dig2 3 6"]

# 풀이 1 람다와 + 연산자를 이용 : 요구 조건을 얼마나 깔끔하게 처리할 수 있는지를 묻는 문제
def reorderLogFiles(logs): 
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit(): 
            digits.append(log)
        else: 
            letters.append(log)
    # 문자로 구성된 로그가 숫자 로그보다 이전에 오며, 숫자 로그는 입력 순서대로 둔다.
    # 문자와 숫자를 구분하고, 숫자는 나중에 이어 붙인다.
    # 숫자 로그도 문자열이다.
    # isdigit() : 숫자 여부 판별

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    # 식별자를 제외한 문자열 [1:]을 키로하여 정렬, 동일한 경우 후순위로 식별자 [0]을 지정해 정렬하도록 함 
    return letters + digits

# 결과
print(reorderLogFiles(logs))