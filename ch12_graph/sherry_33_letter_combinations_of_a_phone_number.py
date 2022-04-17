#!/usr/bin/python3
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

# 문제 33 전화 번호 문자 조합 : 2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.

# 예제
input = "23" # 출력: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# 풀이 1 모든 조합 탐색 전체를 탐색하여 풀이한다. 
# 전체로 탐색한 후 백트래킹하면서 결과를 조합한다.

def letterCombinations(digits):
    def dfs(index, path):
        # 끝까지 탐색하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return

        # 입력값 자릿수 단위 반복
        for i in range(index, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    # 예외 처리
    if not digits:
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"} # 키판 배열
    result = []
    dfs(0, "")

    return result

print(letterCombinations(input))