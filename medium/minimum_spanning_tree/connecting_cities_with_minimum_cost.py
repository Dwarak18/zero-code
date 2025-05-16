import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
import heapq

class Solution:
    def minimumCost(self, n, connections):
        parent = list(range(n+1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        connections.sort(key=lambda x: x[2])
        total = 0
        count = 0
        for u, v, w in connections:
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                total += w
                count += 1
        return total if count == n-1 else -1

    def test_minimumCost(self):
        test_cases = [
            (3, [(1,2,5),(1,3,6),(2,3,1)], 6),
            (4, [(1,2,3),(3,4,4)], -1),
            (4, [(1,2,1),(2,3,2),(3,4,4),(1,4,3)], 6),
            (5, [(1,2,1),(2,3,2),(3,4,3),(4,5,4),(1,5,10)], 10),
            (2, [(1,2,1)], 1),
            (2, [(1,2,2)], 2),
            (3, [(1,2,1),(2,3,2)], 3),
            (3, [(1,2,1),(2,3,2),(1,3,2)], 3),
            (3, [(1,2,1)], -1),
            (4, [(1,2,1),(2,3,2),(3,4,3)], 6),
            (4, [(1,2,1),(2,3,2),(3,4,3),(1,4,1)], 4),
            (4, [(1,2,1),(2,3,2),(3,4,3),(1,4,10)], 6),
            (4, [(1,2,1),(2,3,2),(3,4,3),(1,4,1),(2,4,1)], 4),
            (5, [(1,2,1),(2,3,2),(3,4,3),(4,5,4),(1,5,1)], 7),
            (5, [(1,2,1),(2,3,2),(3,4,3),(4,5,4),(1,5,10),(2,5,1)], 7),
            (5, [(1,2,1),(2,3,2),(3,4,3),(4,5,4),(1,5,10),(2,5,1),(3,5,1)], 7),
            (5, [(1,2,1),(2,3,2),(3,4,3),(4,5,4),(1,5,10),(2,5,1),(3,5,1),(4,5,1)], 7),
            (5, [(1,2,1),(2,3,2),(3,4,3),(4,5,4),(1,5,10),(2,5,1),(3,5,1),(4,5,1),(1,3,1)], 6),
            (5, [(1,2,1),(2,3,2),(3,4,3),(4,5,4),(1,5,10),(2,5,1),(3,5,1),(4,5,1),(1,3,1),(1,4,1)], 5),
        ]
        passed = 0
        for idx, (n, connections, expected) in enumerate(test_cases, 1):
            result = self.minimumCost(n, connections)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({n}, {connections}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_minimumCost()

if __name__ == "__main__":
    run_tests()
