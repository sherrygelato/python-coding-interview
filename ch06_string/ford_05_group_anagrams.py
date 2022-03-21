#!/usr/bin/python3
"""
CH06. 05_Group_Anagrams
"""

strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']


# --------------------------------------------------
import collections


def groupAnagram(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


print(groupAnagram(strs))
