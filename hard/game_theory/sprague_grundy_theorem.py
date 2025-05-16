import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def grundy(self, n):
        # Example: Grundy numbers for the game of Nim with heap size n
        return n

    def test_grundy(self):
        test_cases = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (13, 13),
            (14, 14),
            (15, 15),
            (16, 16),
            (17, 17),
            (18, 18),
            (19, 19),
        ]
        passed = 0
        for idx, (n, expected) in enumerate(test_cases, 1):
            result = self.grundy(n)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={n}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_grundy()

if __name__ == "__main__":
    run_tests()
