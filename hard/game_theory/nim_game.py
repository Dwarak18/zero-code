import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def canWinNim(self, n):
        return n % 4 != 0

    def test_canWinNim(self):
        test_cases = [
            (1, True),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, True),
            (7, True),
            (8, False),
            (9, True),
            (10, True),
            (11, True),
            (12, False),
            (13, True),
            (14, True),
            (15, True),
            (16, False),
            (17, True),
            (18, True),
            (19, True),
            (20, False),
        ]
        passed = 0
        for idx, (n, expected) in enumerate(test_cases, 1):
            result = self.canWinNim(n)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={n}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_canWinNim()

if __name__ == "__main__":
    run_tests()
