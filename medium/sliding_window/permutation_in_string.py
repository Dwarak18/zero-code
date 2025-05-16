import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        s1_count = Counter(s1)
        window = Counter(s2[:len1])
        if window == s1_count:
            return True
        for i in range(len1, len2):
            window[s2[i]] += 1
            window[s2[i-len1]] -= 1
            if window[s2[i-len1]] == 0:
                del window[s2[i-len1]]
            if window == s1_count:
                return True
        return False

    def test_checkInclusion(self):
        test_cases = [
            ("ab", "eidbaooo", True),
            ("ab", "eidboaoo", False),
            ("adc", "dcda", True),
            ("hello", "ooolleoooleh", False),
            ("a", "a", True),
            ("a", "b", False),
            ("abc", "ccccbbbbaaaa", False),
            ("abc", "bbbca", True),
            ("abc", "cbabcacab", True),
            ("abc", "cbaebabacd", True),
            ("abc", "ab", False),
            ("a", "ab", True),
            ("a", "", False),
            ("", "a", True),
            ("", "", True),
            ("xyz", "afdgzyxksldfm", True),
            ("xyz", "afdgzyxksldf", True),
            ("xyz", "afdgzyxksld", False),
            ("xyz", "afdgzyxksldfmx", True),
            ("xyz", "afdgzyxksldfmxy", True),
        ]
        passed = 0
        for idx, (s1, s2, expected) in enumerate(test_cases, 1):
            result = self.checkInclusion(s1, s2)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({s1}, {s2}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_checkInclusion()

if __name__ == "__main__":
    run_tests()
