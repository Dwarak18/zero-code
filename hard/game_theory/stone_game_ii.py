import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def stoneGameII(self, piles):
        from functools import lru_cache
        n = len(piles)
        suffix = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] + piles[i]
        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0
            res = 0
            for x in range(1, 2*M+1):
                if i+x > n:
                    break
                res = max(res, suffix[i] - dp(i+x, max(M, x)))
            return res
        return dp(0, 1)

    def test_stoneGameII(self):
        test_cases = [
            ([2,7,9,4,4], 10),
            ([1,2,3,4,5,100], 104),
            ([1,2,3,7], 10),
            ([1,2,3,4,5,6,7,8,9,10], 36),
            ([1], 1),
            ([1,2], 3),
            ([1,2,3], 4),
            ([1,2,3,4], 6),
            ([1,2,3,4,5], 9),
            ([1,2,3,4,5,6], 12),
            ([1,2,3,4,5,6,7], 16),
            ([1,2,3,4,5,6,7,8], 20),
            ([1,2,3,4,5,6,7,8,9], 25),
            ([1,2,3,4,5,6,7,8,9,10,11], 41),
            ([1,2,3,4,5,6,7,8,9,10,11,12], 46),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13], 52),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 58),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 65),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 72),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], 80),
        ]
        passed = 0
        for idx, (piles, expected) in enumerate(test_cases, 1):
            result = self.stoneGameII(piles)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={piles}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_stoneGameII()

if __name__ == "__main__":
    run_tests()
