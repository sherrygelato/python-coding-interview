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

# 문제 04 가장 흔한 단어 : 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표. 쉼표 등) 또한 무시한다.

# 예제
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
banned = ["hit"]
# “ball"

# 풀이 1 : 리스트 컴프리헨션, Counter 객체 사용
def mostCommonWord(paragraph, banned): 
    # Data Cleansing 입력값에 대한 전처리(Preprocessing) : 입력값에는 대소문자가 섞여 있으며 쉼표 등 구두점이 존재하기에, 데이터 클렌징 작업이 필요하다.
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned]
    # 정규식을 섞어쓰면 더 편리하다.
    #   - \w : 단어 문자 Word Character
    #   - ^ : not
    #   - 해당 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역할이다.
    #   - 리스트 컴프리헨션의 조건절 : banned에 포함되지 않은 단어만을 대상
    
    # 각 단어의 갯수
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]
    # 딕셔너리 변수인 counts에서 값이 가장 큰 키를 가져온다.

# 결과
print(mostCommonWord(paragraph, banned))