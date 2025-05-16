import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def sortedSquares(self, A: list[int]) -> list[int]:
        return sorted([x*x for x in A])

    def test_sorted_squares(self):
        test_cases = [
            ([-4,-1,0,3,10], [0,1,9,16,100]),
            ([-7,-3,2,3,11], [4,9,9,49,121]),
            ([0], [0]),
            ([1], [1]),
            ([-1], [1]),
            ([1,2,3,4,5], [1,4,9,16,25]),
            ([-5,-4,-3,-2,-1], [1,4,9,16,25]),
            ([0,1,2,3,4,5], [0,1,4,9,16,25]),
            ([-5,-3,-1,0,2,4,6], [0,1,4,9,16,25,36]),
            ([2,3,4,5,6], [4,9,16,25,36]),
            ([-6,-5,-4,-3,-2], [4,9,16,25,36]),
            ([0,0,0,0], [0,0,0,0]),
            ([1,1,1,1], [1,1,1,1]),
            ([-1,-1,-1,-1], [1,1,1,1]),
            ([1,2,2,3,3,4], [1,4,4,9,9,16]),
            ([-4,-3,-2,-1,0,1,2,3,4], [0,1,1,4,4,9,9,16,16]),
            ([10,20,30,40,50], [100,400,900,1600,2500]),
            ([-10,-20,-30,-40,-50], [100,400,900,1600,2500]),
            ([0,1,2,3,4,5,6,7,8,9,10], [0,1,4,9,16,25,36,49,64,81,100]),
            ([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0], [0,1,4,9,16,25,36,49,64,81,100]),
        ]
        passed = 0
        for idx, (A, expected) in enumerate(test_cases, 1):
            result = self.sortedSquares(A)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_sorted_squares()

if __name__ == "__main__":
    run_tests()
