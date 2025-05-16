import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    def test_max_subarray(self):
        test_cases = [
            ([-2,1,-3,4,-1,2,1,-5,4], 6),
            ([1], 1),
            ([5,4,-1,7,8], 23),
            ([1,2,3,4,5], 15),
            ([-1,-2,-3,-4], -1),
            ([0,0,0,0], 0),
            ([1,-1,1,-1,1,-1,1], 1),
            ([2,-1,2,3,4,-5], 10),
            ([1,2,-1,2,1,-5,4], 5),
            ([3,-2,5,-1], 6),
            ([1,2,3,-2,5], 9),
            ([1,-2,3,10,-4,7,2,-5], 18),
            ([1,2,3,4,-10,5,6,7,8], 26),
            ([1,-1,1,-1,1,-1,1,-1,1], 1),
            ([1,2,3,-2,5,-3,2,2], 10),
            ([1,2,3,4,5,-15,10,10], 20),
            ([1,2,3,4,5,-15,10,10,-5,10], 25),
            ([1,2,3,4,5,-15,10,10,-5,10,10], 35),
            ([1,2,3,4,5,-15,10,10,-5,10,10,10], 45),
            ([1,2,3,4,5,-15,10,10,-5,10,10,10,10], 55),
        ]
        passed = 0
        for idx, (nums, expected) in enumerate(test_cases, 1):
            result = self.maxSubArray(nums)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_max_subarray()

if __name__ == "__main__":
    run_tests()
