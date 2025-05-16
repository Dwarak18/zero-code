import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance

class Solution:
    def kruskal(self, n, edges):
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return False
            parent[yr] = xr
            return True
        mst = []
        edges.sort(key=lambda x: x[2])
        for u, v, w in edges:
            if union(u, v):
                mst.append((u, v, w))
                if len(mst) == n - 1:
                    break
        return mst

    def test_kruskal(self):
        test_cases = [
            (4, [(0,1,1),(1,2,2),(0,2,3),(2,3,4)], [(0,1,1),(1,2,2),(2,3,4)]),
            (3, [(0,1,1),(1,2,2),(0,2,3)], [(0,1,1),(1,2,2)]),
            (2, [(0,1,1)], [(0,1,1)]),
            (5, [(0,1,1),(1,2,2),(2,3,3),(3,4,4),(4,0,5)], [(0,1,1),(1,2,2),(2,3,3),(3,4,4)]),
            (4, [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)], [(2,3,4),(0,3,5),(0,1,10)]),
            (3, [(0,1,1),(1,2,1),(0,2,2)], [(0,1,1),(1,2,1)]),
            (4, [(0,1,1),(1,2,1),(2,3,1),(3,0,1)], [(0,1,1),(1,2,1),(2,3,1)]),
            (3, [(0,1,2),(1,2,2),(0,2,1)], [(0,2,1),(0,1,2)]),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4)], [(0,1,1),(1,2,2),(2,3,3)]),
            (5, [(0,1,1),(1,2,2),(2,3,3),(3,4,4),(4,0,5),(1,3,1)], [(0,1,1),(1,3,1),(1,2,2),(2,3,3)]),
            (2, [(0,1,2)], [(0,1,2)]),
            (3, [(0,1,1),(1,2,1),(0,2,1)], [(0,1,1),(1,2,1)]),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4),(0,2,5)], [(0,1,1),(1,2,2),(2,3,3)]),
            (3, [(0,1,1),(1,2,2),(0,2,3),(2,0,1)], [(0,1,1),(2,0,1)]),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4),(0,2,5),(1,3,1)], [(0,1,1),(1,3,1),(1,2,2),(2,3,3)]),
            (2, [(0,1,1),(1,0,1)], [(0,1,1)]),
            (3, [(0,1,1),(1,2,2),(0,2,3),(2,0,1)], [(0,1,1),(2,0,1)]),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4),(0,2,5),(1,3,1),(2,0,1)], [(0,1,1),(1,3,1),(2,0,1),(1,2,2)]),
            (3, [(0,1,1),(1,2,2),(0,2,3),(2,0,1),(1,0,1)], [(0,1,1),(1,0,1)]),
            (4, [(0,1,1),(1,2,2),(2,3,3),(3,0,4),(0,2,5),(1,3,1),(2,0,1),(3,1,1)], [(0,1,1),(1,3,1),(2,0,1),(3,1,1)]),
        ]
        passed = 0
        for idx, (n, edges, expected) in enumerate(test_cases, 1):
            result = self.kruskal(n, edges)
            if sorted(result) == sorted(expected):
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({n}, {edges}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_kruskal()

if __name__ == "__main__":
    run_tests()
