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
# from typing import *

# 문제 31 상위 k번 이상 등장하는 요소를 추출하라.
# 입력
nums = [1, 1, 1, 2, 2, 3]
k = 2
# 출력 : [1, 2]

# 풀이 1 counter를 이용한 음수 순 추출
# 1) 요소의 값을 키로 하는 해시 테이블을 만들고 
# 2) 빈도 수를 저장, 
# 3) 우선순위 큐를 이용해 상위 k번만큼 추출 => k번 이상 등장하는 요소 추출

def topKFrequent1(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []
    
    for f in freqs:
        # 매번 삽입하면 매번 heapify()로 인해 별도 처리할 필요가 없고, 힙의 삽입 방식이다.
        heapq.heappush(freqs_heap, (-freqs[f], f))
        # 키/값을 바꿔서 힙에 추가 => 키 순서대로 정렬되기 때문에 이를 위해 빈도수를 키로 함

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    
    return topk

print(topKFrequent1(nums, k))

# 풀이 2 파이썬다운 방식

def topKFrequent2(nums, k):
    # * : 시퀀스 언팩킹 연산자
    return list(list(zip(*collections.Counter(nums).most_common(k)))[0])

print(topKFrequent2(nums, k))