import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def canJump(self, nums):
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
        return True

    def test_canJump(self):
        test_cases = [
            ([2,3,1,1,4], True),
            ([3,2,1,0,4], False),
            ([0], True),
            ([2,0,0], True),
            ([1,2,3], True),
            ([1,0,1,0], False),
            ([2,5,0,0], True),
            ([1,1,1,1,1], True),
            ([1,1,0,1], False),
            ([2,0,6,9,8,4,5,0,8,9,1,2,1,2,6,5,1,2,6,3], True),
            ([1,2,0,1,0,2,0], True),
            ([1,1,1,0], True),
            ([1,0,0,0], False),
            ([2,0,0,0], True),
            ([0,2,3], False),
            ([2,3,1,1,0,4], False),
            ([2,3,1,1,0,0,4], False),
            ([2,3,1,1,0,0,0,4], False),
            ([2,3,1,1,0,0,0,0,4], False),
            ([2,3,1,1,0,0,0,0,0,4], False),
        ]
        passed = 0
        for idx, (nums, expected) in enumerate(test_cases, 1):
            result = self.canJump(nums)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={nums}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_canJump()

if __name__ == "__main__":
    run_tests()
