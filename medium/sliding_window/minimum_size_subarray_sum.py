import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len

    def test_minSubArrayLen(self):
        test_cases = [
            (7, [2,3,1,2,4,3], 2),
            (4, [1,4,4], 1),
            (11, [1,2,3,4,5], 3),
            (15, [1,2,3,4,5], 5),
            (100, [1,2,3,4,5], 0),
            (3, [1,1], 0),
            (6, [10,2,3], 1),
            (8, [2,3,1,2,4,3], 3),
            (5, [1,2,3,4,5], 2),
            (11, [1,2,3,4,5,6,7,8,9,10], 2),
            (15, [1,2,3,4,5,6,7,8,9,10], 2),
            (21, [1,2,3,4,5,6,7,8,9,10], 3),
            (1, [1,2,3,4,5], 1),
            (2, [1,1,1,1,1,1,1,1], 2),
            (7, [1,2,3,4,5], 2),
            (3, [1,1,1,1,1,1,1,1], 3),
            (4, [1,4,4,1], 1),
            (5, [2,3,1,2,4,3], 2),
            (6, [1,2,3,4,5], 2),
            (7, [1,2,3,4,5,6,7,8,9,10], 1),
        ]
        passed = 0
        for idx, (target, nums, expected) in enumerate(test_cases, 1):
            result = self.minSubArrayLen(target, nums)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({target}, {nums}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_minSubArrayLen()

if __name__ == "__main__":
    run_tests()
