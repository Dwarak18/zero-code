import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def test_two_sum(self):
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([1, 2, 3, 4, 5], 9, [3, 4]),
            ([0, 4, 3, 0], 0, [0, 3]),
            ([-1, -2, -3, -4, -5], -8, [2, 4]),
            ([1, 5, 1, 5], 10, [1, 3]),
            ([1, 2], 3, [0, 1]),
            ([1, 2, 3], 7, None),
            ([2, 5, 5, 11], 10, [1, 2]),
            ([1, 3, 4, 2], 6, [2, 3]),
            ([1, 2, 3, 4, 4], 8, [3, 4]),
            ([1, 2, 3, 4, 5, 6], 11, [4, 5]),
            ([1, 2, 3, 4, 5, 6], 7, [0, 5]),
            ([1, 2, 3, 4, 5, 6], 2, None),
            ([1, 2, 3, 4, 5, 6], 12, None),
            ([1, 2, 3, 4, 5, 6], 5, [0, 3]),
            ([1, 2, 3, 4, 5, 6], 9, [2, 5]),
            ([1, 2, 3, 4, 5, 6], 10, [3, 5]),
            ([1, 2, 3, 4, 5, 6], 8, [1, 5]),
        ]
        passed = 0
        for idx, (nums, target, expected) in enumerate(test_cases, 1):
            result = self.twoSum(nums, target)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_two_sum()

if __name__ == "__main__":
    run_tests()