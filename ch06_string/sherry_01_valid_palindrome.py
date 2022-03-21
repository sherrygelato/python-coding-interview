# -*- coding:UTF-8 -*-

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import Deque

class Solution:
    # 문제 01 유효한 팰린드롬 : 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

    # 예제
    s11 = "A man, a plan, a canal: Panama" # True
    s12 = "race a car" # False

    # 풀이 1 리스트로 변환
    def isPaltndrome1(s):

        # 문자열을 입력받아 팰린드롬 여부 판별
        #   - 대소문자 여부 구분 안함
        #   - 영문자, 숫자만을 대상으로 함
        
        # 전처리
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        # - isalnum() : 영문자, 숫자 여부 판별
        # - lower() : 소문자로 변환
            
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False 
        # - pop() : 인덱스 지정
        # - 맨 뒷부분의 pop() 결과와 매칭하여 일치 않는 경우 False 리턴, 모두 통과 시 True 리턴

        return True
    
    # 결과
    print(isPaltndrome1(s11))
    print(isPaltndrome1(s12))

    # 풀이 2 데크 자료형을 이용한 최적화
    def isPaltndrome2(s):
        
        # Deque를 명시적으로 선언하면 속도를 더 높일 수 있음

        # 자료형 데크로 선언
        Deque = collections.deque()

        for char in s:
            if char.isalnum():
                Deque.append(char.lower())
            
        while len(Deque) > 1:
            if Deque.pop() != Deque.pop():
                return False 

        return True
    
    # 결과
    print(isPaltndrome2(s11))
    print(isPaltndrome2(s12))

    # 풀이 3 슬라이싱 사용
    def isPaltndrome3(s): 

        # - 정규식으로 불필요한 문자를 필터링하고,
        #    - 문자열 전체를 한 번에 영숫자Alphanumeric만 걸러내도록 정규식 처리
        # - 슬라이싱으로 문자열을 조작했다.
        #   - [::-1]을 하면 뒤집을 수 있다. 
            
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1] # 슬라이싱

    # 결과
    print(isPaltndrome3(s11))
    print(isPaltndrome3(s12))

    # 문법 : 문자열 슬라이싱
    s13 = "안녕하세요"

    print(s13[1:4])
    print(s13[1:-2])
    print(s13[1:])
    print(s13[:])
    print(s13[1:100])
    print(s13[-1])
    print(s13[-4])
    print(s13[:-3])
    print(s13[-3:])
    print(s13[::-1])
    print(s13[::2])
