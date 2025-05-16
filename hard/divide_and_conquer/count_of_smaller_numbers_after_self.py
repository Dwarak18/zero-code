import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def countSmaller(self, nums):
        res = [0] * len(nums)
        def sort(enum):
            mid = len(enum) // 2
            if mid:
                left, right = sort(enum[:mid]), sort(enum[mid:])
                m, n = len(left), len(right)
                i = j = 0
                merged = []
                while i < m or j < n:
                    if j == n or (i < m and left[i][1] <= right[j][1]):
                        res[left[i][0]] += j
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                return merged
            else:
                return enum
        sort(list(enumerate(nums)))
        return res

    def test_countSmaller(self):
        test_cases = [
            ([5,2,6,1], [2,1,1,0]),
            ([2,0,1], [2,0,0]),
            ([1,2,3,4,5], [0,0,0,0,0]),
            ([5,4,3,2,1], [4,3,2,1,0]),
            ([1], [0]),
            ([1,1,1,1], [0,0,0,0]),
            ([1,2,1,2,1], [0,2,0,1,0]),
            ([3,2,2,6,1], [3,1,1,1,0]),
            ([1,3,2,3,1], [0,2,1,1,0]),
            ([2,9,7,8,5], [0,3,1,1,0]),
            ([5,2,6,1,3], [3,1,2,0,0]),
            ([5,2,6,1,3,4], [4,1,3,0,0,0]),
            ([5,2,6,1,3,4,7], [5,1,4,0,0,0,0]),
            ([5,2,6,1,3,4,7,8], [6,1,5,0,0,0,0,0]),
            ([5,2,6,1,3,4,7,8,9], [7,1,6,0,0,0,0,0,0]),
            ([5,2,6,1,3,4,7,8,9,10], [8,1,7,0,0,0,0,0,0,0]),
            ([5,2,6,1,3,4,7,8,9,10,11], [9,1,8,0,0,0,0,0,0,0,0]),
            ([5,2,6,1,3,4,7,8,9,10,11,12], [10,1,9,0,0,0,0,0,0,0,0,0]),
            ([5,2,6,1,3,4,7,8,9,10,11,12,13], [11,1,10,0,0,0,0,0,0,0,0,0,0]),
        ]
        passed = 0
        for idx, (nums, expected) in enumerate(test_cases, 1):
            result = self.countSmaller(nums)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input={nums}, expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_countSmaller()

if __name__ == "__main__":
    run_tests()
