import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from measure_performance import measure_performance

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #write your code here    
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
        
    def test_max_profit(self):
        test_cases = [
            ([7,1,5,3,6,4], 5),
            ([7,6,4,3,1], 0),
            ([1,2,3,4,5], 4),
            ([2,4,1], 2),
            ([3,3,5,0,0,3,1,4], 4),
            ([1,2], 1),
            ([2,1,2,1,0,1,2], 2),
            ([1,2,4,2,5,7,2,4,9,0], 8),
            ([2,1,4], 3),
            ([1,2,3,4,5,6,7,8,9,10], 9),
            ([10,9,8,7,6,5,4,3,2,1], 0),
            ([1,1,1,1,1,1,1,1,1,1], 0),
            ([1,2,1,2,1,2,1,2,1,2], 1),
            ([2,4,1,7], 6),
            ([1,2,3,2,1,0,1,2,3,4], 4),
            ([3,2,6,5,0,3], 4),
            ([1,7,5,3,6,4,8,2,5], 7),
            ([2,1,2,0,1], 1),
            ([1,2,3,4,5,0,1,2,3,4], 4),
            ([1,2,3,4,5,6,7,8,9,10,1], 9),
        ]
        passed = 0
        for idx, (prices, expected) in enumerate(test_cases, 1):
            result = self.maxProfit(prices)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: got {result}, expected {expected}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_max_profit()

if __name__ == "__main__":
    run_tests()
