import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import Counter

class Solution:
    def fourSumCount(self, A, B, C, D):
        countAB = Counter(a + b for a in A for b in B)
        return sum(countAB.get(-(c + d), 0) for c in C for d in D)

    def test_fourSumCount(self):
        test_cases = [
            ([1,2], [-2,-1], [-1,2], [0,2], 2),
            ([0], [0], [0], [0], 1),
            ([1,1], [-1,-1], [0,1], [0,-1], 4),
            ([1,2,3], [4,5,6], [7,8,9], [10,11,12], 0),
            ([0,1,2], [0,1,2], [0,1,2], [0,1,2], 19),
            ([1,-1], [-1,1], [1,-1], [-1,1], 16),
            ([1,2,3,4], [-1,-2,-3,-4], [0,0,0,0], [0,0,0,0], 64),
            ([1,2], [2,1], [-1,-2], [-2,-1], 8),
            ([1,2,3], [-3,-2,-1], [0,0,0], [0,0,0], 27),
            ([1,2,3,4,5], [-5,-4,-3,-2,-1], [0,0,0,0,0], [0,0,0,0,0], 125),
            ([1,2,3,4,5], [1,2,3,4,5], [-1,-2,-3,-4,-5], [-1,-2,-3,-4,-5], 625),
            ([1], [1], [1], [-3], 1),
            ([1,2], [2,3], [-2,-3], [-1,-2], 8),
            ([0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], 256),
            ([1,2,3,4], [1,2,3,4], [-1,-2,-3,-4], [-1,-2,-3,-4], 256),
            ([1,2,3], [1,2,3], [-1,-2,-3], [-1,-2,-3], 81),
            ([1,2], [1,2], [-1,-2], [-1,-2], 16),
            ([1], [1], [-1], [-1], 1),
            ([1,2,3,4,5,6,7,8,9,10], [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], 10000),
        ]
        passed = 0
        for idx, (A, B, C, D, expected) in enumerate(test_cases, 1):
            result = self.fourSumCount(A, B, C, D)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({A}, {B}, {C}, {D}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_fourSumCount()

if __name__ == "__main__":
    run_tests()
