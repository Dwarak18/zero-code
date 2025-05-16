import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from measure_performance import measure_performance
from collections import defaultdict

class Solution:
    def countComponents(self, n, edges):
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        for u, v in edges:
            union(u, v)
        return len(set(find(x) for x in range(n)))

    def test_countComponents(self):
        test_cases = [
            (5, [[0,1],[1,2],[3,4]], 2),
            (5, [[0,1],[1,2],[2,3],[3,4]], 1),
            (5, [], 5),
            (1, [], 1),
            (2, [[1,0]], 1),
            (2, [], 2),
            (3, [[0,1]], 2),
            (3, [[0,1],[1,2]], 1),
            (4, [[0,1],[2,3]], 2),
            (4, [[0,1],[1,2],[2,3]], 1),
            (6, [[0,1],[1,2],[3,4],[4,5]], 2),
            (6, [[0,1],[1,2],[2,3],[3,4],[4,5]], 1),
            (7, [[0,1],[1,2],[3,4],[5,6]], 3),
            (7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], 1),
            (8, [[0,1],[1,2],[3,4],[5,6],[6,7]], 3),
            (8, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], 1),
            (10, [[0,1],[2,3],[4,5],[6,7],[8,9]], 5),
            (10, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], 1),
            (10, [], 10),
            (10, [[0,1],[2,3],[4,5],[6,7],[8,9],[1,2],[3,4],[5,6],[7,8]], 1),
        ]
        passed = 0
        for idx, (n, edges, expected) in enumerate(test_cases, 1):
            result = self.countComponents(n, edges)
            if result == expected:
                print(f"Test case {idx} passed.")
                passed += 1
            else:
                print(f"Test case {idx} failed: input=({n}, {edges}), expected={expected}, got={result}")
        print(f"Passed {passed}/{len(test_cases)} test cases.")

@measure_performance
def run_tests():
    sol = Solution()
    sol.test_countComponents()

if __name__ == "__main__":
    run_tests()
