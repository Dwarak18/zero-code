import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def maxSumSubarrayOfSizeK(self, nums: list[int], k: int) -> int:
        if not nums or k > len(nums):
            return 0
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum

    def test_maxSumSubarrayOfSizeK(self):
        test_cases = [
            ([2,1,5,1,3,2], 3, 9),
            ([2,3,4,1,5], 2, 7),
            ([1,2,3,4,5,6,7,8,9,10], 5, 40),
            ([1,2,3,4,5], 1, 5),
            ([1,2,3,4,5], 5, 15),
            ([1,2,3,4,5], 6, 0),
            ([5,5,5,5,5], 3, 15),
            ([1,2,3,4,5,6,7,8,9,10], 10, 55),
            ([1,2,3,4,5,6,7,8,9,10], 9, 54),
            ([1,2,3,4,5,6,7,8,9,10], 8, 52),
            ([1,2,3,4,5,6,7,8,9,10], 7, 49),
            ([1,2,3,4,5,6,7,8,9,10], 6, 45),
            ([1,2,3,4,5,6,7,8,9,10], 4, 34),
            ([1,2,3,4,5,6,7,8,9,10], 3, 27),
            ([1,2,3,4,5,6,7,8,9,10], 2, 19),
            ([1,2,3,4,5,6,7,8,9,10], 1, 10),
            ([1,2,3,4,5,6,7,8,9,10], 0, 0),
            ([1], 1, 1),
            ([1], 2, 0),
            ([1,2], 2, 3),
        ]
        passed = 0
        for idx, (nums, k, expected) in enumerate(test_cases, 1):
            result = self.maxSumSubarrayOfSizeK(nums, k)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({nums}, {k}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_maxSumSubarrayOfSizeK()

if __name__ == "__main__":
    run_tests()
