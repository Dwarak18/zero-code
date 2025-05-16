import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from measure_performance import measure_performance

class Solution:
    def intersect(self, nums1, nums2):
        from collections import Counter
        c1, c2 = Counter(nums1), Counter(nums2)
        result = []
        for num in c1:
            if num in c2:
                result.extend([num] * min(c1[num], c2[num]))
        return result

    @measure_performance
    def test_intersect(self):
        test_cases = [
            ([1,2,2,1], [2,2], [2,2]),
            ([4,9,5], [9,4,9,8,4], [4,9]),
            ([1,2,2,1], [2], [2]),
            ([1,2,2,1], [3], []),
            ([1], [1], [1]),
            ([1,2,2,1], [1,1], [1,1]),
            ([1,2,2,1], [2,2,2], [2,2]),
            ([1,2,3,4,5], [6,7,8,9], []),
            ([1,1,1,1], [1,1], [1,1]),
            ([2,2,2], [2,2], [2,2]),
            ([1,2,3], [1,1,1,2,2,3,3], [1,2,3]),
            ([1,2,2,3], [2,2,3,3], [2,2,3]),
            ([1,2,3,4], [2,4,6,8], [2,4]),
            ([1,2,2,1], [1,2,2,1], [1,2,2,1]),
            ([1,2,2,1], [], []),
            ([], [1,2,2,1], []),
            ([1,2,2,1], [2,1], [1,2]),
            ([1,2,2,1], [2,2,2,2], [2,2]),
            ([1,2,2,1], [1,1,1,1], [1,1]),
            ([1,2,2,1], [2,2,1,1], [1,2,2,1]),
        ]
        passed = 0
        for i, (nums1, nums2, expected) in enumerate(test_cases):
            result = self.intersect(nums1, nums2)
            if sorted(result) == sorted(expected):
                print(f"Test case {i+1} passed.")
                passed += 1
            else:
                print(f"Test case {i+1} failed: input=({nums1}, {nums2}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

if __name__ == "__main__":
    Solution().test_intersect()
