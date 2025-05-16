import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []
        for i in range(word_len):
            left = i
            curr_count = Counter()
            count = 0
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                if word in word_count:
                    curr_count[word] += 1
                    count += 1
                    while curr_count[word] > word_count[word]:
                        curr_count[s[left:left+word_len]] -= 1
                        left += word_len
                        count -= 1
                    if count == len(words):
                        res.append(left)
                else:
                    curr_count.clear()
                    count = 0
                    left = j + word_len
        return res

    def test_findSubstring(self):
        test_cases = [
            ("barfoothefoobarman", ["foo","bar"], [0,9]),
            ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
            ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
            ("wordgoodgoodgoodbestword", ["good","good","best","word"], [8]),
            ("", ["a"], []),
            ("a", [], []),
            ("", [], []),
            ("foobarfoobar", ["foo","bar"], [0,3,6]),
            ("abababab", ["ab","ba"], [0,2]),
            ("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"], [13]),
            ("aaaaaaaaaaaaaa", ["aa","aa"], [0,1,2,3,4,5,6,7,8,9,10]),
            ("mississippi", ["is","si"], [1,4]),
            ("mississippi", ["is","is"], [1]),
            ("mississippi", ["si","is"], [1,4]),
            ("mississippi", ["pp","ss"], []),
            ("mississippi", ["pp","ii"], []),
            ("mississippi", ["pp","pi"], [8]),
            ("mississippi", ["ss","pp"], []),
            ("mississippi", ["ss","pi"], [5]),
            ("mississippi", ["pi","ss"], [5]),
        ]
        passed = 0
        for idx, (s, words, expected) in enumerate(test_cases, 1):
            result = self.findSubstring(s, words)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({s}, {words}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_findSubstring()

if __name__ == "__main__":
    run_tests()
