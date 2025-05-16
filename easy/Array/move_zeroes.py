import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index += 1
        for i in range(zero_index, len(nums)):
            nums[i] = 0
        return nums

    def test_move_zeroes(self):
        test_cases = [
            ([0,1,0,3,12], [1,3,12,0,0]),
            ([0,0,1], [1,0,0]),
            ([1,0,1], [1,1,0]),
            ([0,0,0,0], [0,0,0,0]),
            ([1,2,3,4], [1,2,3,4]),
            ([0,1,2,0,3,0,4], [1,2,3,4,0,0,0]),
            ([1,0,0,2,0,3], [1,2,3,0,0,0]),
            ([0,0,1,0,0,2,0,0,3], [1,2,3,0,0,0,0,0,0]),
            ([1,2,0,0,3,4,0,5], [1,2,3,4,5,0,0,0]),
            ([0,1,0,2,0,3,0,4,0,5], [1,2,3,4,5,0,0,0,0,0]),
            ([1,0,2,0,3,0,4,0,5,0], [1,2,3,4,5,0,0,0,0,0]),
            ([0,0,0,1], [1,0,0,0]),
            ([1,0,0,0], [1,0,0,0]),
            ([0,1,0,0], [1,0,0,0]),
            ([1,0,0,0,0], [1,0,0,0,0]),
            ([0,0,0,0,1], [1,0,0,0,0]),
            ([1,2,0,0,0,3,4,0,5], [1,2,3,4,5,0,0,0,0]),
            ([0,0,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,0,0]),
            ([1,0,0,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0,0,0]),
            ([0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]),
        ]
        passed = 0
        for idx, (nums, expected) in enumerate(test_cases, 1):
            arr = nums[:]
            self.moveZeroes(arr)
            if arr == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {arr}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_move_zeroes()

if __name__ == "__main__":
    run_tests()
