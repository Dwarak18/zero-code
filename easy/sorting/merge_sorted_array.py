import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    def test_merge(self):
        test_cases = [
            ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
            ([1], 1, [], 0, [1]),
            ([0], 0, [1], 1, [1]),
            ([2,0], 1, [1], 1, [1,2]),
            ([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6]),
            ([1,2,4,5,6,0], 5, [3], 1, [1,2,3,4,5,6]),
            ([1,0,0,0], 1, [2,3,4], 3, [1,2,3,4]),
            ([0,0,0], 0, [2,5,6], 3, [2,5,6]),
            ([1,2,3,0,0,0], 3, [4,5,6], 3, [1,2,3,4,5,6]),
            ([1,2,3,0,0,0], 3, [1,2,3], 3, [1,1,2,2,3,3]),
            ([1,2,3,0,0,0], 3, [0,0,0], 3, [0,0,0,1,2,3]),
            ([0,0,0,0], 0, [1,2,3,4], 4, [1,2,3,4]),
            ([1,0,0,0,0], 1, [2,3,4,5], 4, [1,2,3,4,5]),
            ([1,2,0,0,0], 2, [3,4,5], 3, [1,2,3,4,5]),
            ([1,2,3,4,0,0,0,0], 4, [5,6,7,8], 4, [1,2,3,4,5,6,7,8]),
            ([1,2,3,4,0,0,0,0], 4, [1,2,3,4], 4, [1,1,2,2,3,3,4,4]),
            ([1,2,3,4,0,0,0,0], 4, [0,0,0,0], 4, [0,0,0,0,1,2,3,4]),
            ([0,0,0,0,0], 0, [1,2,3,4,5], 5, [1,2,3,4,5]),
            ([1,0,0,0,0,0], 1, [2,3,4,5,6], 5, [1,2,3,4,5,6]),
            ([1,2,0,0,0,0], 2, [3,4,5,6], 4, [1,2,3,4,5,6]),
        ]
        passed = 0
        for idx, (nums1, m, nums2, n, expected) in enumerate(test_cases, 1):
            arr1 = nums1[:]
            self.merge(arr1, m, nums2, n)
            if arr1 == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {arr1}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_merge()

if __name__ == "__main__":
    run_tests()
