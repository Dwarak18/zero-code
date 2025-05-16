import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def test_binary_search(self):
        test_cases = [
            ([1,2,3,4,5], 3, 2),
            ([1,2,3,4,5], 1, 0),
            ([1,2,3,4,5], 5, 4),
            ([1,2,3,4,5], 6, -1),
            ([1], 1, 0),
            ([1], 0, -1),
            ([1,3,5,7,9], 7, 3),
            ([1,3,5,7,9], 2, -1),
            ([1,2], 2, 1),
            ([1,2], 1, 0),
            ([1,2], 3, -1),
            ([1,2,3,4,5,6,7,8,9,10], 10, 9),
            ([1,2,3,4,5,6,7,8,9,10], 1, 0),
            ([1,2,3,4,5,6,7,8,9,10], 5, 4),
            ([1,2,3,4,5,6,7,8,9,10], 11, -1),
            ([1,2,3,4,5,6,7,8,9,10], -1, -1),
            ([2,4,6,8,10], 8, 3),
            ([2,4,6,8,10], 5, -1),
            ([2,4,6,8,10], 2, 0),
            ([2,4,6,8,10], 10, 4),
        ]
        passed = 0
        for idx, (nums, target, expected) in enumerate(test_cases, 1):
            result = self.binarySearch(nums, target)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_binary_search()

if __name__ == "__main__":
    run_tests()
