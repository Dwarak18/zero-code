import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def test_search_insert(self):
        test_cases = [
            ([1,3,5,6], 5, 2),
            ([1,3,5,6], 2, 1),
            ([1,3,5,6], 7, 4),
            ([1,3,5,6], 0, 0),
            ([1], 0, 0),
            ([1], 1, 0),
            ([1], 2, 1),
            ([1,2,3,4,5], 3, 2),
            ([1,2,3,4,5], 6, 5),
            ([1,2,3,4,5], 0, 0),
            ([1,2,3,4,5], 1, 0),
            ([1,2,3,4,5], 5, 4),
            ([1,2,3,4,5], 4, 3),
            ([1,2,3,4,5], 2, 1),
            ([1,2,3,4,5], -1, 0),
            ([1,2,3,4,5], 10, 5),
            ([2,4,6,8,10], 5, 2),
            ([2,4,6,8,10], 8, 3),
            ([2,4,6,8,10], 1, 0),
            ([2,4,6,8,10], 11, 5),
        ]
        passed = 0
        for idx, (nums, target, expected) in enumerate(test_cases, 1):
            result = self.searchInsert(nums, target)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_search_insert()

if __name__ == "__main__":
    run_tests()
