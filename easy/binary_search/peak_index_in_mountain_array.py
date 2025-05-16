import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

    def test_peak_index(self):
        test_cases = [
            ([0,1,0], 1),
            ([0,2,1,0], 1),
            ([0,10,5,2], 1),
            ([3,4,5,1], 2),
            ([24,69,100,99,79,78,67,36,26,19], 2),
            ([1,2,3,4,5,3,1], 4),
            ([0,1,2,3,4,5,6,7,8,9,10,5,2], 10),
            ([18,29,38,59,98,100,99,98,90], 5),
            ([0,1,2,3,2,1,0], 3),
            ([0,2,4,6,8,10,8,6,4,2,0], 5),
            ([1,3,5,7,6,4,2], 3),
            ([2,4,6,8,10,9,7,5,3,1], 4),
            ([0,5,10,5,0], 2),
            ([0,2,1,0], 1),
            ([0,1,0], 1),
            ([1,3,2], 1),
            ([0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0], 9),
            ([0,1,2,3,4,3,2,1,0], 4),
            ([0,1,0], 1),
            ([0,2,1,0], 1),
        ]
        passed = 0
        for idx, (arr, expected) in enumerate(test_cases, 1):
            result = self.peakIndexInMountainArray(arr)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_peak_index()

if __name__ == "__main__":
    run_tests()
