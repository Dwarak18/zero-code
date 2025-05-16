import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    def test_longest_common_prefix(self):
        test_cases = [
            (["flower","flow","flight"], "fl"),
            (["dog","racecar","car"], ""),
            (["interspace","internet","internal"], "inte"),
            (["a"], "a"),
            (["",""], ""),
            (["abc","abc","abc"], "abc"),
            (["abc","ab","a"], "a"),
            (["abc","def","ghi"], ""),
            (["prefix","preach","prevent"], "pre"),
            (["a","b","c"], ""),
            (["abcde","abc","abcd"], "abc"),
            (["abc","abcd","abce"], "abc"),
            (["abc","abcde","abcdef"], "abc"),
            (["abc","abc","abcabc"], "abc"),
            (["abc","abc","abcabcabc"], "abc"),
            (["abc","abcabc","abcabcabc"], "abc"),
            (["abc","abcabcabc","abcabcabcabc"], "abc"),
            (["abc","abcabcabcabc","abcabcabcabcabc"], "abc"),
            (["abc","abcabcabcabcabc","abcabcabcabcabcabc"], "abc"),
            (["abc","abcabcabcabcabcabc","abcabcabcabcabcabcabc"], "abc"),
        ]
        passed = 0
        for idx, (strs, expected) in enumerate(test_cases, 1):
            result = self.longestCommonPrefix(strs)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_longest_common_prefix()

if __name__ == "__main__":
    run_tests()
