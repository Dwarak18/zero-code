import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        

    def test_rotate(self):
        test_cases = [
            ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
            ([1,2,3,4,5,6,7], 1, [7,1,2,3,4,5,6]),
            ([1,2,3,4,5,6,7], 7, [1,2,3,4,5,6,7]),
            ([1,2,3,4,5,6,7], 0, [1,2,3,4,5,6,7]),
            ([1,2,3,4,5,6,7], 2, [6,7,1,2,3,4,5]),
            ([1,2,3,4,5,6,7], 4, [4,5,6,7,1,2,3]),
            ([1,2,3,4,5,6,7], 5, [3,4,5,6,7,1,2]),
            ([1,2,3,4,5,6,7], 6, [2,3,4,5,6,7,1]),
            ([1,2,3,4,5,6,7], 8, [7,1,2,3,4,5,6]),
            ([1,2,3,4,5,6,7], 10, [5,6,7,1,2,3,4]),
            ([1,2,3,4,5,6,7], 14, [1,2,3,4,5,6,7]),
            ([1,2,3,4,5,6,7], 13, [2,3,4,5,6,7,1]),
            ([1,2,3,4,5,6,7], 12, [3,4,5,6,7,1,2]),
            ([1,2,3,4,5,6,7], 11, [4,5,6,7,1,2,3]),
            ([1,2,3,4,5,6,7], 9, [6,7,1,2,3,4,5]),
            ([1,2,3,4,5,6,7], 15, [7,1,2,3,4,5,6]),
            ([1,2,3,4,5,6,7], 16, [6,7,1,2,3,4,5]),
            ([1,2,3,4,5,6,7], 17, [5,6,7,1,2,3,4]),
            ([1,2,3,4,5,6,7], 18, [4,5,6,7,1,2,3]),
            ([1,2,3,4,5,6,7], 19, [3,4,5,6,7,1,2]),
        ]
        passed = 0
        for idx, (nums, k, expected) in enumerate(test_cases, 1):
            arr = nums[:]
            self.rotate(arr, k)
            if arr == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {arr}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_rotate()

if __name__ == "__main__":
    run_tests()
