import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][n-1] >= 0

    def test_PredictTheWinner(self):
        test_cases = [
            ([1,5,2], False),
            ([1,5,233,7], True),
            ([1], True),
            ([1,2], True),
            ([1,2,3], True),
            ([1,2,3,4], False),
            ([1,2,3,4,5], True),
            ([1,2,3,4,5,6], True),
            ([1,2,3,4,5,6,7], True),
            ([1,2,3,4,5,6,7,8], True),
            ([1,2,3,4,5,6,7,8,9], True),
            ([1,2,3,4,5,6,7,8,9,10], True),
            ([1,2,3,4,5,6,7,8,9,10,11], True),
            ([1,2,3,4,5,6,7,8,9,10,11,12], True),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13], True),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], True),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], True),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], True),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], True),
        ]
        passed = 0
        for idx, (nums, expected) in enumerate(test_cases, 1):
            result = self.PredictTheWinner(nums)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={nums}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_PredictTheWinner()

if __name__ == "__main__":
    run_tests()
