"""
CH16. 57_Palindrome_Pairs.py
"""

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# 입력 1 
input1 = ['abcd', 'dcba', 'lls', 's', 'sssll']
# 출력 1
output1 = [[0, 1], [1, 0], [2, 4], [3, 2]]

# 입력 2 
input2 = ['bat', 'tab', 'cat']
# 출력 2
output2 = [[0,1], [1,0]]

# 입력 3 
input3 = ['d', 'cbbcd', 'dcbb', 'dcbc', 'cbbc', 'bbcd']
# 출력 3
output3 = [[0, 1], [1, 4], [2, 5], [2, 1], [3, 0], [5, 2]]


# --------------------------------------------------
def palindromePairs(words):
    def is_palindrome(word):
        return word == word[::-1]
    
    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])
    return output


print(palindromePairs(input1))
print(sorted(palindromePairs(input1)) == sorted(output1))
print(palindromePairs(input2))
print(sorted(palindromePairs(input2)) == sorted(output2))
print(palindromePairs(input3))
print(sorted(palindromePairs(input3)) == sorted(output3))


# --------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()


    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]


    # 단어 삽입
    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index


    def search(self, index, word):
        result = []
        node = self.root
        
        while word:
            # 판별로직 3
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        
        # 판별로직 1
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        
        # 판별로직 2
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        
        return result



def palindromePairs2(words):
    trie = Trie()
    
    for i, word in enumerate(words):
        trie.insert(i, word)
    
    results = []
    for i, word in enumerate(words):
        results.extend(trie.search(i, word))
    
    return results


print(palindromePairs2(input1))
print(sorted(palindromePairs2(input1)) == sorted(output1))
print(palindromePairs2(input2))
print(sorted(palindromePairs2(input2)) == sorted(output2))
print(palindromePairs2(input3))
print(sorted(palindromePairs2(input3)) == sorted(output3))


# --------------------------------------------------