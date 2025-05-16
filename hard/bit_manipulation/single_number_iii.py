import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def singleNumber(self, nums):
        x = 0
        for n in nums:
            x ^= n
        return x

    def singleNumberIII(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        diff = xor & -xor
        x = 0
        for n in nums:
            if n & diff:
                x ^= n
        return [x, xor ^ x]

    def test_singleNumberIII(self):
        test_cases = [
            ([1,2,1,3,2,5], [3,5]),
            ([2,1,2,3], [1,3]),
            ([0,1], [0,1]),
            ([1,2], [1,2]),
            ([1,1,2,2,3,4], [3,4]),
            ([1,2,1,3,2,5,6,7], [6,7]),
            ([1,2,1,3,2,5,6,7,8,9], [8,9]),
            ([1,2,1,3,2,5,6,7,8,9,10,11], [10,11]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13], [12,13]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15], [14,15]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17], [16,17]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], [18,19]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], [20,21]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], [22,23]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], [24,25]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27], [26,27]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], [28,29]),
            ([1,2,1,3,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], [30,31]),
        ]
        passed = 0
        for idx, (nums, expected) in enumerate(test_cases, 1):
            result = sorted(self.singleNumberIII(nums))
            if result == sorted(expected):
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={nums}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_singleNumberIII()

if __name__ == "__main__":
    run_tests()
