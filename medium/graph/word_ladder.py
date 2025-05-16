import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, length + 1))
        return 0

    def test_ladderLength(self):
        test_cases = [
            ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
            ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
            ("a", "c", ["a","b","c"], 2),
            ("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"], 4),
            ("lost", "cost", ["most","fist","lost","cost","fish"], 2),
            ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
            ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
            ("a", "c", ["a","b","c"], 2),
            ("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"], 4),
            ("lost", "cost", ["most","fist","lost","cost","fish"], 2),
            ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
            ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
            ("a", "c", ["a","b","c"], 2),
            ("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"], 4),
            ("lost", "cost", ["most","fist","lost","cost","fish"], 2),
            ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
            ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
            ("a", "c", ["a","b","c"], 2),
            ("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"], 4),
            ("lost", "cost", ["most","fist","lost","cost","fish"], 2),
        ]
        passed = 0
        for idx, (beginWord, endWord, wordList, expected) in enumerate(test_cases, 1):
            result = self.ladderLength(beginWord, endWord, wordList)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({beginWord}, {endWord}, {wordList}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_ladderLength()

if __name__ == "__main__":
    run_tests()
