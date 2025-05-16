import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def sortArrayByParity(self, A: list[int]) -> list[int]:
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 != 0]

    def test_sort_array_by_parity(self):
        test_cases = [
            ([3,1,2,4], [2,4,3,1]),
            ([0], [0]),
            ([1], [1]),
            ([2,4,6,8], [2,4,6,8]),
            ([1,3,5,7], [1,3,5,7]),
            ([2,1], [2,1]),
            ([1,2], [2,1]),
            ([2,2,2,1,1,1], [2,2,2,1,1,1]),
            ([1,1,1,2,2,2], [2,2,2,1,1,1]),
            ([2,1,4,3], [2,4,1,3]),
            ([1,2,3,4,5,6], [2,4,6,1,3,5]),
            ([6,5,4,3,2,1], [6,4,2,5,3,1]),
            ([1,3,5,2,4,6], [2,4,6,1,3,5]),
            ([2,1,2,1,2,1], [2,2,2,1,1,1]),
            ([1,2,1,2,1,2], [2,2,2,1,1,1]),
            ([2,2,2,2,2,2], [2,2,2,2,2,2]),
            ([1,1,1,1,1,1], [1,1,1,1,1,1]),
            ([2,1,3,4,5,6,7,8,9,10], [2,4,6,8,10,1,3,5,7,9]),
            ([10,9,8,7,6,5,4,3,2,1], [10,8,6,4,2,9,7,5,3,1]),
            ([1,2,3,4,5,6,7,8,9,10], [2,4,6,8,10,1,3,5,7,9]),
        ]
        passed = 0
        for idx, (A, expected) in enumerate(test_cases, 1):
            result = self.sortArrayByParity(A)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_sort_array_by_parity()

if __name__ == "__main__":
    run_tests()
