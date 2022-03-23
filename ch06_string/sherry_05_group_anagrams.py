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

# 문제 05 그룹 애너그램 : 문자열 배열을 받아 애너그램 단위로 그룹핑하라

# 예제
s51 = ["eat", "tea", "tan", "ate", "nat", "bat"] # [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]

# 풀이 1 : 정렬하여 딕셔너리에 추가
def groupAnagrams(strs):
    # 애너그램 판단 기준 : 정렬하여 비교
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
        # sorted()로 문자열 정렬하여 리스트로 리턴, 이를 join()을 이용해 다시 키로 하는 딕셔너리를 구성한다.
        # 애너그램끼리는 같은 키를 갖게 되고, 여기에 append()한다.
    
    return list(anagrams.values())

# 결과
print(groupAnagrams(s51))
