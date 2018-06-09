"""
This is a follow up of Shortest Word Distance. The only difference is now word1
could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance
 between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.

"""
"""
和之前的区别是这两个词可以相等，但是找距离要是不同位置的两个词
solution: 如果这两个词一样，就在同一个list里面找
"""
import collections
class WordDistance():
    def __init__(self, words):
        self.wordIndex = collections.defaultdict(list)
        for i in range(len(words)):
            self.wordIndex[words[i]] == i

    def shortestDistance(self, word1, word2):
        if word1 != word2:
            indexes1 = self.wordIndex[word1]
            indexes2 = self.wordIndex[word2]
            i, j, dist = 0, 0, float('inf')
            while i < len(indexes1) and j < len(indexes2):
                dist = min(dist, abs(indexes1[i] - indexes2[j]))
                if indexes1[i] < indexes2[j]:
                    i += 1
                else:
                    j += 1
        else:
            indexes = self.wordIndex[word1]
            for i in range(len(indexes) - 1):
                dist = min(dist, indexes[i + 1] - indexes[i])

        return dist

# solution 2 without dictionary
class Solution:
    def shortestDistance(self, words, word1, word2):
        dist = float('inf')
        i, index1, index2 = 0, None, None
        is_same = (word1 == words2)
        while i < len(words):
            if words[i] == word1:
                if is_same and index1 is not None:
                    dist = min(dist, (i - index1))
                index1 = i
            elif words[i] == words2:
                index2 = i
            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1
        return dist
