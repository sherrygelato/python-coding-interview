"""
CH16. 56_Implement_Trie(Prefix_Tree).py
"""

import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect


# --------------------------------------------------
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True


    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word


    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# --------------------------------------------------
trie = Trie()
trie.insert('apple')
trie.search('apple')
trie.search('app')
trie.startswith('app')
trie.insert('app')
trie.search('app')