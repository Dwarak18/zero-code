import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())

    def test_groupAnagrams(self):
        test_cases = [
            (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
            ([""], [[""]]),
            (["a"], [["a"]]),
            (["abc","bca","cab","bac","acb","cba"], [["abc","bca","cab","bac","acb","cba"]]),
            (["abc","def","ghi"], [["abc"],["def"],["ghi"]]),
            (["abc","def","cba","fed"], [["abc","cba"],["def","fed"]]),
            (["a","b","c","a"], [["a","a"],["b"],["c"]]),
            (["ab","ba","abc","cab","bac"], [["ab","ba"],["abc","cab","bac"]]),
            (["eat","tea","tan","ate","nat","bat","tab"], [["eat","tea","ate"],["tan","nat"],["bat","tab"]]),
            ([""], [[""]]),
            (["a"], [["a"]]),
            (["abc","bca","cab","bac","acb","cba","def","fed"], [["abc","bca","cab","bac","acb","cba"],["def","fed"]]),
            (["abc","def","ghi","jkl"], [["abc"],["def"],["ghi"],["jkl"]]),
            (["abc","def","cba","fed","ghi","ihg"], [["abc","cba"],["def","fed"],["ghi","ihg"]]),
            (["a","b","c","a","b","c"], [["a","a"],["b","b"],["c","c"]]),
            (["ab","ba","abc","cab","bac","bca"], [["ab","ba"],["abc","cab","bac","bca"]]),
            (["eat","tea","tan","ate","nat","bat","tab","tba"], [["eat","tea","ate"],["tan","nat"],["bat","tab","tba"]]),
            ([""], [[""]]),
            (["a"], [["a"]]),
        ]
        passed = 0
        for idx, (strs, expected) in enumerate(test_cases, 1):
            result = self.groupAnagrams(strs)
            # Convert to sets of frozensets for order-insensitive comparison
            result_set = set(frozenset(g) for g in result)
            expected_set = set(frozenset(g) for g in expected)
            if result_set == expected_set:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={strs}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_groupAnagrams()

if __name__ == "__main__":
    run_tests()
