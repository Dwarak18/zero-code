import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
import random

class Solution:
    def findKthLargest(self, nums, k):
        def quickselect(left, right, k_smallest):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            pivot = nums[right]
            store_index = left
            for i in range(left, right):
                if nums[i] > pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[right], nums[store_index] = nums[store_index], nums[right]
            if store_index == k_smallest:
                return nums[store_index]
            elif store_index < k_smallest:
                return quickselect(store_index + 1, right, k_smallest)
            else:
                return quickselect(left, store_index - 1, k_smallest)
        return quickselect(0, len(nums) - 1, k - 1)

    def test_findKthLargest(self):
        test_cases = [
            ([3,2,1,5,6,4], 2, 5),
            ([3,2,3,1,2,4,5,5,6], 4, 4),
            ([1], 1, 1),
            ([2,1], 2, 1),
            ([2,1], 1, 2),
            ([7,6,5,4,3,2,1], 5, 3),
            ([1,2,3,4,5,6,7], 3, 5),
            ([1,1,1,1,1], 1, 1),
            ([1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10], 10, 5),
            ([10,9,8,7,6,5,4,3,2,1], 1, 10),
            ([10,9,8,7,6,5,4,3,2,1], 10, 1),
            ([1,2,3,4,5,6,7,8,9,10], 5, 6),
            ([1,2,3,4,5,6,7,8,9,10], 1, 10),
            ([1,2,3,4,5,6,7,8,9,10], 10, 1),
            ([1,2,3,4,5,6,7,8,9,10], 2, 9),
            ([1,2,3,4,5,6,7,8,9,10], 3, 8),
            ([1,2,3,4,5,6,7,8,9,10], 4, 7),
            ([1,2,3,4,5,6,7,8,9,10], 6, 5),
            ([1,2,3,4,5,6,7,8,9,10], 7, 4),
        ]
        passed = 0
        for idx, (nums, k, expected) in enumerate(test_cases, 1):
            result = self.findKthLargest(nums[:], k)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({nums}, {k}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_findKthLargest()

if __name__ == "__main__":
    run_tests()
