import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        order = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))

    def test_relative_sort_array(self):
        test_cases = [
            ([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6], [2,2,2,1,4,3,3,9,6,7,19]),
            ([28,6,22,8,44,17], [22,28,8,6], [22,28,8,6,17,44]),
            ([1,2,3,4,5], [2,1,4], [2,1,4,3,5]),
            ([1,2,3,4,5], [5,4,3,2,1], [5,4,3,2,1]),
            ([1,2,3,4,5], [1,2,3], [1,2,3,4,5]),
            ([1,2,3,4,5], [6,7,8], [1,2,3,4,5]),
            ([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6,7,19], [2,2,2,1,4,3,3,9,6,7,19]),
            ([2,3,1,3,2,4,6,7,9,2,19], [], [1,2,2,2,3,3,4,6,7,9,19]),
            ([1,1,1,2,2,2,3,3,3], [3,2,1], [3,3,3,2,2,2,1,1,1]),
            ([1,2,3,4,5,6,7,8,9,10], [2,4,6,8,10], [2,4,6,8,10,1,3,5,7,9]),
            ([1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6], [10,9,8,7,6,1,2,3,4,5]),
            ([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10]),
            ([1,2,3,4,5,6,7,8,9,10], [11,12,13], [1,2,3,4,5,6,7,8,9,10]),
            ([1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1], [10,9,8,7,6,5,4,3,2,1]),
            ([1,2,3,4,5,6,7,8,9,10], [], [1,2,3,4,5,6,7,8,9,10]),
            ([1,1,1,1,1,1,1,1,1,1], [1], [1,1,1,1,1,1,1,1,1,1]),
            ([2,2,2,2,2,2,2,2,2,2], [2], [2,2,2,2,2,2,2,2,2,2]),
            ([1,2,3,4,5,6,7,8,9,10], [5,6,7,8,9,10], [5,6,7,8,9,10,1,2,3,4]),
            ([1,2,3,4,5,6,7,8,9,10], [1,3,5,7,9], [1,3,5,7,9,2,4,6,8,10]),
        ]
        passed = 0
        for idx, (arr1, arr2, expected) in enumerate(test_cases, 1):
            result = self.relativeSortArray(arr1, arr2)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_relative_sort_array()

if __name__ == "__main__":
    run_tests()
