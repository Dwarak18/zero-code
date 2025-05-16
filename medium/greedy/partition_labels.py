import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def partitionLabels(self, s):
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        result = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                result.append(i - anchor + 1)
                anchor = i + 1
        return result

    def test_partitionLabels(self):
        test_cases = [
            ("ababcbacadefegdehijhklij", [9,7,8]),
            ("eccbbbbdec", [10]),
            ("abc", [1,1,1]),
            ("aabbcc", [2,2,2]),
            ("abac", [3,1]),
            ("aaaaa", [5]),
            ("ab", [1,1]),
            ("a", [1]),
            ("abacbc", [6]),
            ("abacbcd", [7]),
            ("abacbcde", [8]),
            ("abacbcdef", [9]),
            ("abacbcdefg", [10]),
            ("abacbcdefgh", [11]),
            ("abacbcdefghi", [12]),
            ("abacbcdefghij", [13]),
            ("abacbcdefghijk", [14]),
            ("abacbcdefghijkl", [15]),
            ("abacbcdefghijklm", [16]),
            ("abacbcdefghijklmn", [17]),
        ]
        passed = 0
        for idx, (s, expected) in enumerate(test_cases, 1):
            result = self.partitionLabels(s)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={s}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_partitionLabels()

if __name__ == "__main__":
    run_tests()
