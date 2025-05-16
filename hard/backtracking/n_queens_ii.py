import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def totalNQueens(self, n):
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                count += backtrack(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col})
            return count
        return backtrack(0, set(), set(), set())

    def test_totalNQueens(self):
        test_cases = [
            (1, 1),
            (2, 0),
            (3, 0),
            (4, 2),
            (5, 10),
            (6, 4),
            (7, 40),
            (8, 92),
            (9, 352),
            (10, 724),
            (11, 2680),
            (12, 14200),
            (13, 73712),
            (14, 365596),
            (15, 2279184),
            (0, 1),
            (16, 14772512),
            (17, 0), # Not calculated, just for test structure
            (18, 0), # Not calculated, just for test structure
            (19, 0), # Not calculated, just for test structure
        ]
        passed = 0
        for idx, (n, expected) in enumerate(test_cases, 1):
            result = self.totalNQueens(n)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={n}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_totalNQueens()

if __name__ == "__main__":
    run_tests()
