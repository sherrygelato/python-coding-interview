"""
CH21. 80_Task_Scheduler.py
"""

import collections
import enum
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# 입력 1
tasks1 = ["A", "A", "A", "B", "B", "B"]
n1 = 2

# 출력 1
output1 = 8


# 입력 2
tasks2 = ["A", "A", "A", "B", "C", "D"]
n2 = 2

# 출력 2
output2 = 7


# --------------------------------------------------
def leastInterval(tasks, n):
    counter = collections.Counter(tasks)
    result = 0
    
    while True:
        sub_count = 0
    
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1
            
            counter.subtract(task)
            counter += collections.Counter()
        
        if not counter:
            break
        
        result += n - sub_count + 1
    
    return result


print(leastInterval(tasks1, n1))
print(leastInterval(tasks1, n1) == output1)
print(leastInterval(tasks2, n2))
print(leastInterval(tasks2, n2) == output2)
