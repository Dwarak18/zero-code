import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])
                return (max_of_left + min_of_right) / 2.0

    def test_findMedianSortedArrays(self):
        test_cases = [
            ([1,3], [2], 2.0),
            ([1,2], [3,4], 2.5),
            ([0,0], [0,0], 0.0),
            ([], [1], 1.0),
            ([2], [], 2.0),
            ([1,2,3], [4,5,6], 3.5),
            ([1,3,5], [2,4,6], 3.5),
            ([1,2,3,4,5], [6,7,8,9,10], 5.5),
            ([1,2,3,4,5,6], [7,8,9,10,11,12], 6.5),
            ([1,2,3,4,5,6,7], [8,9,10,11,12,13,14], 7.5),
            ([1,2,3,4,5,6,7,8], [9,10,11,12,13,14,15,16], 8.5),
            ([1,2,3,4,5,6,7,8,9], [10,11,12,13,14,15,16,17,18], 9.5),
            ([1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20], 10.5),
            ([1,2,3,4,5,6,7,8,9,10,11], [12,13,14,15,16,17,18,19,20,21,22], 11.5),
            ([1,2,3,4,5,6,7,8,9,10,11,12], [13,14,15,16,17,18,19,20,21,22,23,24], 12.5),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13], [14,15,16,17,18,19,20,21,22,23,24,25,26], 13.5),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [15,16,17,18,19,20,21,22,23,24,25,26,27,28], 14.5),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], 15.5),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32], 16.5),
        ]
        passed = 0
        for idx, (nums1, nums2, expected) in enumerate(test_cases, 1):
            result = self.findMedianSortedArrays(nums1, nums2)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({nums1}, {nums2}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_findMedianSortedArrays()

if __name__ == "__main__":
    run_tests()
