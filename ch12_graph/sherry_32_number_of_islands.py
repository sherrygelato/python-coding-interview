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

# 문제 32 섬의 개수 : 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라(연결되어 있는 1의 덩어리 개수를 구하라).

# 예제 
input1 = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
] # 출력 1
input2 = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
] # 출력 3

# 풀이 1 DFS로 그래프 탐색
# 쾨니히스베르크의 다리 문제처럼 반드시 그래프 모양이 아니더라도 그래프형으로 변환해서 풀이할 수 있음을 확인해보는 문제
# 동서남북이 모두 연결된 그래프로 가정하고 동일한 형태로 처리할 수 있다.
# 네 방향 각각 DFS 재귀 이용해 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수 파악 가능하다.

def numIslands(grid):
# 파이썬의 중첩함수는 부모 함수에서 선언한 변수도 유효한 범윈 내에서 사용할 수 있다. 
# numIslands() 함수 내에 dfs() 함수 전체가 중첩 함수로 들어갔다.
    def dfs(i, j):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                # 행렬 입력값인 grid의 행, 열 단위로 육지(1)인 곳을 찾아 진행하다가 발견하면 dfs() 호출하여 탐색 시작한다.
            return

        grid[i][j] = 0

        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1
    return count

print(numIslands(input1))
print(numIslands(input2))