#!/usr/bin/python3
"""
CH06. 04_Most_Common_Work
"""

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


# --------------------------------------------------
import re
import collections

def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() 
             if word not in banned]

    counts = collections.Counter(words)
    print(counts.most_common(1))

    return counts.most_common(1)[0][0]  # list(tuple())형태로 반환.


print(mostCommonWord(paragraph, banned))
