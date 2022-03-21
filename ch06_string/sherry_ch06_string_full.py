#-*- coding:EUC-KR -*-

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
    
    # 예제 1
    s11 = "A man, a plan, a canal: Panama"
    s12 = "race a car"

    # 풀이 1 리스트로 변환
    def isPaltndrome1(s): 

        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
            
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False 

        return True

    # 풀이 2 데크 자료형을 이용한 최적화
    def isPaltndrome2(s): 

        # 자료형 데크로 선언
        Deque = collections.deque(s)

        for char in s:
            if char.isalnum():
                Deque.append(char.lower())
            
        # 팰린드롬 여부 판별
        while len(Deque) > 1:
            if Deque.pop(0) != Deque.pop():
                return False 

        return True

    # 풀이 3 슬라이싱 사용
    def isPaltndrome3(s): 
            
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1] # 슬라이싱

    # 결과
    print(isPaltndrome1(s11))
    print(isPaltndrome2(s11))
    print(isPaltndrome3(s11))
    print(isPaltndrome1(s12))
    print(isPaltndrome2(s12))
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



    # 문제 02 문자열 뒤집기 : 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

    s21 = ["h", "e", "l", "l", "o"]
    s22 = ["H", "a", "n", "n", "a", "h"]

    def reverseString1(self, s): 
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString2(self, s): 
        s.reverse()
    
    # 결과
    print(reverseString1(s21))
    print(reverseString1(s21))
    print(reverseString2(s21))
    print(reverseString2(s22))


    # 문제 03 로그 파일 재정렬 : 로그의 가장 앞 부분은 식별자이며, 문자로 구성된 로그가 숫자 로그보다 앞에 오고, 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 하며, 숫자 로그는 입력 순서대로 한다.

    logs = ["digl 8 1 5 l","letl art can","dig2 3 6","let2 own kit dig","let3 art zero"]

    def reorderLogFiles(logs): 
        letters, digits = [], []

        for log in logs:
            if log.split()[l].isdigit(): 
                digits.append(log)
            else: 
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
    
    # 결과
    print(reorderLogFiles(logs))



    # 문제 04 가장 흔한 단어 : 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표. 쉼표 등) 또한 무시한다.

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
    banned = ["htt"]

    def mostCommonWord(paragraph, banned): 
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned]
        
        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
    
    # 결과
    print(mostCommonWord(paragraph, banned))



    # 문제 05 그룹 애너그램 : 문자열 배열을 받아 애너그램 단위로 그룹핑하라

    s51 = ["eat", "tea", "tan", "ate", "nat", "bat"]

    def groupAnagrams(strs):
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())
    
    # 결과
    print(groupAnagrams(s51))

    # 문제 06 가장 긴 팰린드롬 부분 문자열 : 가장 긴 팰린드롬 부분 문자열을 출력하라.

    # 예제
    s61 = "babad" # "bab", "aba"
    s62 = "cbbd" # "bb"

    # 풀이 1 : 중앙을 중심으로 확장하는 풀이
    def longstPalindrome(self, s):
        
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left, right):
            while left >0 and right < len(s) and s[left] ==s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        
        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(0, len(s) -1):
            reselt = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result
    
    # 결과
    print(longstPalindrome(s61))
    print(longstPalindrome(s62))
