import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def subarraySum(self, nums, k):
        count = {0: 1}
        res = curr = 0
        for n in nums:
            curr += n
            res += count.get(curr - k, 0)
            count[curr] = count.get(curr, 0) + 1
        return res

    def test_subarraySum(self):
        test_cases = [
            ([1,1,1], 2, 2),
            ([1,2,3], 3, 2),
            ([1], 0, 0),
            ([1,-1,0], 0, 3),
            ([3,4,7,2,-3,1,4,2], 7, 4),
            ([1,2,1,2,1], 3, 4),
            ([1,-1,1,-1,1], 0, 4),
            ([1,2,3,4,5], 9, 2),
            ([1,2,3,4,5], 15, 1),
            ([1,2,3,4,5], 1, 1),
            ([1,2,3,4,5], 5, 2),
            ([1,2,3,4,5], 10, 1),
            ([1,2,3,4,5], 14, 0),
            ([1,2,3,4,5], 0, 0),
            ([0,0,0,0,0], 0, 15),
            ([1,-1,1,-1,1,-1,1,-1,1], 0, 16),
            ([1,2,3,4,5,6,7,8,9,10], 10, 1),
            ([1,2,3,4,5,6,7,8,9,10], 55, 1),
            ([1,2,3,4,5,6,7,8,9,10], 100, 0),
            ([1,2,3,4,5,6,7,8,9,10], 0, 0),
        ]
        passed = 0
        for idx, (nums, k, expected) in enumerate(test_cases, 1):
            result = self.subarraySum(nums, k)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({nums}, {k}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_subarraySum()

if __name__ == "__main__":
    run_tests()
