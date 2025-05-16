import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    def test_remove_element(self):
        test_cases = [
            ([3,2,2,3], 3, 2, [2,2]),
            ([0,1,2,2,3,0,4,2], 2, 5, [0,1,3,0,4]),
            ([1], 1, 0, []),
            ([1,2,3,4,5], 6, 5, [1,2,3,4,5]),
            ([1,1,1,1], 1, 0, []),
            ([2,2,2,2], 2, 0, []),
            ([1,2,3,4,5], 3, 4, [1,2,4,5]),
            ([1,2,2,3,4], 2, 3, [1,3,4]),
            ([1,2,3,4,5], 5, 4, [1,2,3,4]),
            ([1,2,3,4,5], 1, 4, [2,3,4,5]),
            ([1,2,3,4,5], 2, 4, [1,3,4,5]),
            ([1,2,3,4,5], 4, 4, [1,2,3,5]),
            ([1,2,3,4,5], 0, 5, [1,2,3,4,5]),
            ([1,1,2,2,3,3,4,4], 3, 6, [1,1,2,2,4,4]),
            ([1,2,3,4,5,1,2,3,4,5], 1, 8, [2,3,4,5,2,3,4,5]),
            ([1,2,3,4,5,1,2,3,4,5], 5, 8, [1,2,3,4,1,2,3,4]),
            ([1,2,3,4,5,1,2,3,4,5], 2, 8, [1,3,4,5,1,3,4,5]),
            ([1,2,3,4,5,1,2,3,4,5], 3, 8, [1,2,4,5,1,2,4,5]),
            ([1,2,3,4,5,1,2,3,4,5], 4, 8, [1,2,3,5,1,2,3,5]),
            ([1,2,3,4,5,1,2,3,4,5], 0, 10, [1,2,3,4,5,1,2,3,4,5]),
        ]
        passed = 0
        for idx, (nums, val, expected_len, expected_arr) in enumerate(test_cases, 1):
            arr = nums[:]
            k = self.removeElement(arr, val)
            if k == expected_len and arr[:k] == expected_arr:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {arr[:k]}, expected {expected_arr}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_remove_element()

if __name__ == "__main__":
    run_tests()
