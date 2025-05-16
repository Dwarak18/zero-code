import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def rangeBitwiseAnd(self, left, right):
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

    def test_rangeBitwiseAnd(self):
        test_cases = [
            (5, 7, 4),
            (0, 0, 0),
            (1, 2147483647, 0),
            (0, 1, 0),
            (10, 11, 10),
            (12, 15, 12),
            (8, 15, 8),
            (6, 7, 6),
            (7, 8, 0),
            (9, 12, 8),
            (13, 15, 12),
            (0, 2, 0),
            (2, 2, 2),
            (3, 3, 3),
            (4, 4, 4),
            (5, 5, 5),
            (6, 6, 6),
            (7, 7, 7),
            (8, 8, 8),
            (9, 9, 9),
        ]
        passed = 0
        for idx, (left, right, expected) in enumerate(test_cases, 1):
            result = self.rangeBitwiseAnd(left, right)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({left}, {right}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_rangeBitwiseAnd()

if __name__ == "__main__":
    run_tests()
