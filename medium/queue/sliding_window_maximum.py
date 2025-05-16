import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []
        dq = deque()
        res = []
        for i, n in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res

    def test_maxSlidingWindow(self):
        test_cases = [
            ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
            ([1], 1, [1]),
            ([9,11], 2, [11]),
            ([4,-2], 2, [4]),
            ([7,2,4], 2, [7,4]),
            ([1,3,1,2,0,5], 3, [3,3,2,5]),
            ([1,3,1,2,0,5], 1, [1,3,1,2,0,5]),
            ([1,3,1,2,0,5], 6, [5]),
            ([1,3,1,2,0,5], 2, [3,3,2,2,5]),
            ([1,2,3,4,5,6,7,8,9,10], 3, [3,4,5,6,7,8,9,10]),
            ([10,9,8,7,6,5,4,3,2,1], 3, [10,9,8,7,6,5,4,3]),
            ([1,2,3,4,5], 2, [2,3,4,5]),
            ([1,2,3,4,5], 5, [5]),
            ([1,2,3,4,5], 1, [1,2,3,4,5]),
            ([1,2,3,4,5], 3, [3,4,5]),
            ([1,2,3,4,5], 4, [4,5]),
            ([1,2,3,4,5], 6, []),
            ([1,2,3,4,5], 0, []),
            ([1,2,3,4,5], 10, []),
        ]
        passed = 0
        for idx, (nums, k, expected) in enumerate(test_cases, 1):
            result = self.maxSlidingWindow(nums, k)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({nums}, {k}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_maxSlidingWindow()

if __name__ == "__main__":
    run_tests()
