import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index

    def test_remove_duplicates(self):
        test_cases = [
            ([1,1,2], 2),
            ([0,0,1,1,1,2,2,3,3,4], 5),
            ([1,2,3,4,5], 5),
            ([1,1,1,1,1], 1),
            ([1,2,2,3,3,3,4,4,4,4], 4),
            ([1], 1),
            ([], 0),
            ([2,2,2,2,2,2,2,2,2,2], 1),
            ([1,2,2,2,3,4,4,5,5,6], 6),
            ([1,1,2,2,3,3,4,4,5,5], 5),
            ([1,2,3,3,3,4,5,5,6,7], 7),
            ([1,1,1,2,2,3,3,4,4,5], 5),
            ([1,2,3,4,4,4,5,6,7,8], 8),
            ([1,1,2,3,4,5,6,7,8,9], 9),
            ([1,2,3,4,5,5,5,5,5,5], 5),
            ([1,2,3,3,3,3,3,3,3,3], 3),
            ([1,1,1,1,1,1,1,1,1,2], 2),
            ([1,2,2,2,2,2,2,2,2,2], 2),
        ]
        passed = 0
        for idx, (nums, expected_length) in enumerate(test_cases, 1):
            arr = nums[:]
            length = self.removeDuplicates(arr)
            if length == expected_length:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {length}, expected {expected_length}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_remove_duplicates()

if __name__ == "__main__":
    run_tests()
